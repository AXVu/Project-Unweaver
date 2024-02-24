from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PictureForm

def upload_picture(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to homepage after successful upload
    else:
        form = PictureForm()
    return render(request, 'upload_picture.html', {'form': form})

def index(request):
    return HttpResponse("Hello, world!")