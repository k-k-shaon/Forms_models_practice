from django.shortcuts import render, redirect
from .forms import Add_Book

# Create your views here.

def models(request):
    if request.method == 'POST':
        form = Add_Book(request.POST)
        if form.is_valid():
            form.save()
            return redirect('models')
    else:
        form = Add_Book()
    return render(request, 'models.html', {'form': form})
