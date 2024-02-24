from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PictureForm
from myapp.barcode_reader import file_to_brand
import pandas as pd
from django.apps import apps

def upload_picture(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save()
            pic_path = picture.image.path
            brand = file_to_brand(pic_path)
            return HttpResponse(f"Brand is: {brand}. This brand is: {brand_check(brand)}")  # Redirect to homepage after successful upload
    else:
        form = PictureForm()
    return render(request, 'upload_picture.html', {'form': form})

def index(request):
    return HttpResponse("Hello, world!")

def brand_check(brand):
    my_config = apps.get_app_config("myapp")
    df = my_config.data
    df = df.loc[df["Brand Name"] == brand]
    if df.shape[0] > 0:
        return df.to_numpy()[0][0]
    else:
        return f"{brand} not in database"
