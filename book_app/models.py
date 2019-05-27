from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENRE =(
    ('Unknown','unknown'),
    ('Historical','historical'),
    ('Romance','romance'),
    ('Action','action'),
    ('Thriller','thriller'),
    ('Comedy','comedy'),
    ('Manga_comics','manga_comics'),
    ('Fiction','fiction'),
    ('Paranomal','Paranomal'),

)
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    year_of_publish = models.CharField(max_length=10)
    cover =models.ImageField()
    genre =models.CharField(choices=GENRE, max_length=30, default='unknown')
    content = models.FileField(default='')


    def __str__(self):
        return self.title


class Book_itself(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title

class Authors(models.Model):
    author_pic = models.ImageField()
    name=models.CharField(max_length=40)


    def __str__(self):
        return self.name