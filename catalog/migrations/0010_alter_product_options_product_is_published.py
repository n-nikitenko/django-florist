# Generated by Django 4.2.14 on 2024-07-19 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_product_creator'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('can_change_description', 'может менять описание'), ('can_change_category', 'может менять категорию'), ('can_change_is_published', 'может менять признак публикации')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Признак публикации'),
        ),
    ]