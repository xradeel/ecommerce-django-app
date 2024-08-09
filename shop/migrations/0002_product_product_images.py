# Generated by Django 5.0.7 on 2024-07-31 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('short_description', models.TextField(max_length=500)),
                ('long_description', models.TextField()),
                ('size', models.CharField(max_length=255)),
                ('availability', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=False)),
                ('popular', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('thumbnail1', models.ImageField(upload_to='thumbnails/')),
                ('thumbnail2', models.ImageField(upload_to='thumbnails/')),
                ('accesstoken', models.CharField(max_length=255)),
                ('tag', models.CharField(max_length=255)),
                ('createdat', models.DateTimeField(auto_now_add=True)),
                ('updatedat', models.DateTimeField(auto_now=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Product_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='product-images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='shop.product')),
            ],
        ),
    ]