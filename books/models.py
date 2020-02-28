from django.db import models

class Publisher(models.Model):
    name = models.CharField(primary_key=True, max_length=200)  # Field name made lowercase.
    address = models.TextField(blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=20)  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'publisher'

class Author(models.Model):
    author_name = models.CharField(primary_key=True, max_length=200)  # Field name made lowercase.
    date_of_birth = models.DateField()  # Field name made lowercase.

    works_for = models.ManyToManyField(Publisher, related_name='authors')

    def __str__(self):
        return self.author_name
    class Meta:
        managed = True
        db_table = 'author'


class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=15)  # Field name made lowercase.
    title = models.CharField(max_length=200)  # Field name made lowercase.
    published_date = models.DateField()  # Field name made lowercase.
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)  # Field name made lowercase.

    written = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return f'{self.isbn} {self.title}'
    class Meta:
        managed = True
        db_table = 'book'