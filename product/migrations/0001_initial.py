# Generated by Django 5.0.6 on 2024-06-20 05:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('stock', models.CharField(choices=[('in_stock', 'В наличии'), ('out_stock', 'Нет в наличии')], max_length=50)),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='category.category')),
                ('onwer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Товары',
                'verbose_name_plural': 'Тoвары',
            },
        ),
    ]