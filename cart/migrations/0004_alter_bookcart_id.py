# Generated by Django 5.0.4 on 2024-05-01 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20240501_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcart',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
