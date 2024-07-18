# Generated by Django 4.2.13 on 2024-07-17 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_alter_contacts_address_alter_product_price_and_more")
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="catalog.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="preview",
            field=models.ImageField(
                blank=True, null=True, upload_to="", verbose_name="Изображение"
            ),
        ),
    ]