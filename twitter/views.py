from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile, Tweet, Follow, Like, Comment

# 1. Tela de Cadastro de novos usuários
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Verifica se o usuário já existe no banco
        if User.objects.filter(username=username).exists():
            return render(request, 'twitter/register.html', {'error': 'Este usuário já existe.'})
            
        # Cria o usuário e o seu perfil associado automaticamente
        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user)
        
        # Faz login automático após o cadastro e joga para o Feed
        login(request, user)
        return redirect('feed')
        
    return render(request, 'twitter/register.html')

# 2. Tela de Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'twitter/login.html', {'error': 'Usuário ou senha incorretos.'})
            
    return render(request, 'twitter/login.html')

# 3. Função de Logout (Sair da conta)
def logout_view(request):
    logout(request)
    return redirect('login')

# 4. O Feed principal (Atualizado para salvar e listar tweets)
@login_required(login_url='login')
def feed_view(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Tweet.objects.create(user=request.user, content=content)
            return redirect('feed')

    # Busca todos os tweets do banco para exibir no feed global inicialmente
    tweets = Tweet.objects.all()
    return render(request, 'twitter/feed.html', {'tweets': tweets})

    # 6. Função para Curtir / Descurtir um Post
@login_required(login_url='login')
def like_toggle_view(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    
    # Verifica se o usuário já curtiu esse tweet
    like_exist = Like.objects.filter(user=request.user, tweet=tweet)
    
    if like_exist.exists():
        like_exist.delete() # Se já curtiu, remove a curtida
    else:
        Like.objects.create(user=request.user, tweet=tweet) # Se não curtiu, adiciona
        
    return redirect('feed')

# 5. Função para Seguir / Deixar de Seguir um Usuário
@login_required(login_url='login')
def follow_toggle_view(request, user_id):
    user_to_follow = User.objects.get(id=user_id)
    follow_exist = Follow.objects.filter(user_from=request.user, user_to=user_to_follow)
    
    if follow_exist.exists():
        follow_exist.delete()
    else:
        Follow.objects.create(user_from=request.user, user_to=user_to_follow)
        
    return redirect('feed')

    # 7. Função para Adicionar um Comentário a um Post
@login_required(login_url='login')
def add_comment_view(request, tweet_id):
    if request.method == 'POST':
        content = request.POST.get('comment_content')
        if content:
            tweet = Tweet.objects.get(id=tweet_id)
            Comment.objects.create(user=request.user, tweet=tweet, content=content)
    return redirect('feed')

# 8. Tela de Perfil, Listagem de Seguidores e Edição de Dados
@login_required(login_url='login')
def profile_view(request):
    success = False
    profile = request.user.profile
    
    if request.method == 'POST':
        username = request.POST.get('username')
        bio = request.POST.get('bio')
        password = request.POST.get('password')
        profile_picture = request.POST.get('profile_picture') # Campo para URL da foto
        
        user = request.user
        if username and username != user.username:
            if not User.objects.filter(username=username).exists():
                user.username = username
        
        if password:
            user.set_password(password)
            
        user.save()
        
        # Atualiza a biografia e a foto
        profile.bio = bio
        if profile_picture:
            profile.profile_picture = profile_picture
        profile.save()
        
        if password:
            login(request, user)
            
        success = True
    
    # Busca a lista real de Seguidores e Seguidos exigida pelo professor
    seguidores = Follow.objects.filter(user_to=request.user)
    seguidos = Follow.objects.filter(user_from=request.user)
        
    return render(request, 'twitter/profile.html', {
        'success': success,
        'seguidores': seguidores,
        'seguidos': seguidos
    })




