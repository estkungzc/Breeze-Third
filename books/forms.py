from django import forms

from .models import Book, Author, Publisher
import datetime

class BookForm(forms.ModelForm):
    published_date = forms.DateField(initial=datetime.date.today)
    class Meta:
        model = Book
        fields = '__all__'


class AuthorForm(forms.ModelForm):
    date_of_birth = forms.DateField(initial=datetime.date.today)
    class Meta:
        model = Author
        fields = '__all__'


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'