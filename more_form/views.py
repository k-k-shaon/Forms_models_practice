from django.shortcuts import render
from .forms import ExampleForm

# Create your views here.

def forms(request):
    form = ExampleForm()
    return render(request, 'forms.html', {'form': form})