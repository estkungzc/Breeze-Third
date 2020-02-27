# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Publisher(models.Model):
    name = models.CharField(primary_key=True, max_length=200)  # Field name made lowercase.
    address = models.TextField(blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=20)  # Field name made lowercase.
Authoe
    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'publisher'

class Author(models.Model):
    author_name = models.CharField(primary_key=True, max_length=200)  # Field name made lowercase.
    date_of_birth = models.DateField()  # Field name made lowercase.

    works_for = models.ManyToManyField(Publisher)

    class Meta:
        managed = True
        db_table = 'author'


class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=15)  # Field name made lowercase.
    title = models.CharField(max_length=200)  # Field name made lowercase.
    published_date = models.DateField()  # Field name made lowercase.
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)  # Field name made lowercase.

    written = models.ManyToManyField(Author)

    class Meta:
        managed = True
        db_table = 'book'

