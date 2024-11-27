# Generated by Django 5.0.4 on 2024-05-03 21:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_bookcart_id'),
        ('product', '0006_alter_book_id_alter_genre_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookFacture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.book')),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id_Facture', models.AutoField(primary_key=True, serialize=False)),
                ('book', models.ManyToManyField(through='cart.BookFacture', to='product.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bookfacture',
            name='facture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.facture'),
        ),
        migrations.AddConstraint(
            model_name='bookfacture',
            constraint=models.UniqueConstraint(fields=('Facture', 'book'), name='unique_book_in_Facture'),
        ),
    ]
