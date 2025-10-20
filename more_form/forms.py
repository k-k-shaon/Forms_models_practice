from django import forms
from django.forms.widgets import NumberInput
import datetime

years = ['2001', '2002', '2003']
colors= [('b', 'Blue'),('g', 'Green'),('bl', 'Black')]
hobbieslist=[('r', 'Reading'),('t', 'Traveling'),('c', 'Coding')]

class MoreForm(forms.Form):
    name = forms.CharField(label="Enter your full name")
    comment = forms.CharField(widget=forms.Textarea, label="Describe yourself")
    email = forms.EmailField(label="Enter email address")
    agree = forms.BooleanField(initial=True, label="My informations are correct")
    date = forms.DateField(initial=datetime.date.today, label="Submission date")
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}),label="Your Birthday")
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=years),label="Birth date")
    favorite_color = forms.ChoiceField(choices=colors,label="Choose Your Favorite Color")
    hobbies = forms.MultipleChoiceField(choices=hobbieslist,widget=forms.CheckboxSelectMultiple,label="Select Your Hobbies")
    salary = forms.DecimalField(max_digits=6,decimal_places=2,label="Expected Salary")
