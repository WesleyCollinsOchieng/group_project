# Generated by Django 2.2.1 on 2019-05-23 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=40)),
                ('year_of_publish', models.CharField(max_length=10)),
                ('cover', models.ImageField(upload_to='')),
                ('genre', models.CharField(choices=[('Unknown', 'unknown'), ('Historical', 'historical'), ('Romance', 'romance'), ('Action', 'action'), ('Thriller', 'thriller'), ('Comedy', 'comedy'), ('Manga_comics', 'manga_comics'), ('Fiction', 'fiction'), ('Paranomal', 'Paranomal')], default='unknown', max_length=30)),
                #('content', models.FileField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book_itself',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_app.Book')),
            ],
        ),
    ]
