# Generated by Django 3.1 on 2024-05-01 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_bookcart_unique_book_in_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcart',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
