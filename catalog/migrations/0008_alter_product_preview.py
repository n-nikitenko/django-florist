# Generated by Django 4.2.13 on 2024-07-17 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("catalog", "0007_alter_product_category_alter_product_preview")]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="preview",
            field=models.ImageField(upload_to="", verbose_name="Изображение"),
        )
    ]