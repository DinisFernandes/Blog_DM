from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    subtitle = models.CharField(max_length=255, verbose_name='Sub titulo')
    content = models.TextField(verbose_name='Conteudo')
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data')
    image = models.ImageField(upload_to='post_img/%Y/%m/%d',blank=True, null=True, verbose_name='Imagem')
    publicated = models.BooleanField(default=False, verbose_name='Publicado')

    def __str__(self):
        return self.title