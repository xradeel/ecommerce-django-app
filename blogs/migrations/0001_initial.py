# Generated by Django 5.0.7 on 2024-07-31 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('published', models.BooleanField(default=True)),
                ('accesstoken', models.CharField(max_length=250)),
                ('tags', models.CharField(max_length=250)),
                ('summary', models.CharField(max_length=250)),
                ('read_time', models.IntegerField(max_length=11)),
                ('image', models.ImageField(upload_to='blogs/')),
                ('createdat', models.DateTimeField(auto_now_add=True)),
                ('updatedat', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]