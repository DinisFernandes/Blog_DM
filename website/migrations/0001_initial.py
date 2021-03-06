# Generated by Django 3.0.7 on 2020-06-27 13:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('subtitle', models.CharField(max_length=255, verbose_name='Sub titulo')),
                ('content', models.TextField(verbose_name='Conteudo')),
                ('data_post', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_img/%Y/%m/%d', verbose_name='Imagem')),
                ('publicated', models.BooleanField(default=False, verbose_name='Publicado')),
            ],
        ),
    ]
