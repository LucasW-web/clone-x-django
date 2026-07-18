from django.db import models
from django.contrib.auth.models import User

# 1. Perfil do Usuário (Para foto de perfil e biografia)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.png', blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

# 2. Modelo de Tweet (Postagem)
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    content = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] # Mostra sempre os mais novos primeiro

    def __str__(self):
        return f'{self.user.username}: {self.content[:30]}'

# 3. Modelo de Seguidores (Quem segue quem)
class Follow(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_from', 'user_to') # Impede seguir a mesma pessoa duas vezes

    def __str__(self):
        return f'{self.user_from} segue {self.user_to}'

# 4. Modelo de Curtidas
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('user', 'tweet') # Impede curtir o mesmo tweet duas vezes

# 5. Modelo de Comentários
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} comentou no tweet de {self.tweet.user.username}'