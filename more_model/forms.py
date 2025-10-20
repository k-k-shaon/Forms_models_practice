from django import forms
from .models import Book

class Add_Book(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
