# Generated by Django 2.2.1 on 2019-05-23 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='content',
            field=models.FileField(default='', upload_to=''),
        ),
    ]