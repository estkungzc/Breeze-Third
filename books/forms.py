from django import forms

from .models import Book
import datetime

class BookForm(forms.ModelForm):
    published_date = forms.DateField(initial=datetime.date.today)
    class Meta:
        model = Book
        fields = '__all__'