from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='Название книги')
    author = models.CharField(max_length=100, verbose_name='Автор книги')
    published_year = models.PositiveIntegerField(verbose_name='Год издания')
    isbn = models.CharField(max_length=13)
    caption = models.CharField(verbose_name='Описание книги')

    def __str__(self):
        return f'{self.id}  {self.title}, {self.published_year} - {self.author}'
