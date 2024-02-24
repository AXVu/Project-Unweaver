from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PictureForm
from myapp.barcode_reader import file_to_brand

def upload_picture(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save()
            pic_path = picture.image.path
            
            return HttpResponse(f"Brand is: {file_to_brand(pic_path)}")  # Redirect to homepage after successful upload
    else:
        form = PictureForm()
    return render(request, 'upload_picture.html', {'form': form})

def index(request):
    return HttpResponse("Hello, world!")