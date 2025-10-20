from django.shortcuts import render
from .forms import MoreForm

# Create your views here.

def forms(request):
    form = MoreForm()
    return render(request, 'forms.html', {'form': form})