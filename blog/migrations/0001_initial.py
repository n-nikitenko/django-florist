# Generated by Django 4.2.13 on 2024-06-19 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('slug', models.CharField(max_length=200, null=True, verbose_name='slug')),
                ('content', models.TextField(verbose_name='Содержимое')),
                ('preview', models.ImageField(null=True, upload_to='', verbose_name='Изображение')),
                ('is_published', models.BooleanField(default=False, verbose_name='Признак публикации')),
                ('views_count', models.IntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата/время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата/время обновления')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
