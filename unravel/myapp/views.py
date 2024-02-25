from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PictureForm
from myapp.barcode_reader import file_to_brand
import pandas as pd
from django.apps import apps
from django.conf import settings
import os

def upload_picture(request):
    brand = ""
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        
        if form.is_valid():
            picture = form.save()
            request.session['image_url'] = picture.image.url
            brand = file_to_brand(picture.image.path)
            return render(request, 'upload_picture.html', {'form': form, 'image_url': picture.image.url, "brand": brand, "sus": brand_check(brand)})
    else:
        form = PictureForm()
    
    image_url = request.session.get('image_url', None)

    return render(request, 'upload_picture.html', {'form': form, 'image_url': image_url, "brand": brand, "sus": brand_check(brand)})

def index(request):
    return HttpResponse("Hello, world!")    

def brand_check(brand):
    my_config = apps.get_app_config("myapp")
    df = my_config.data
    df = df.loc[df["Brand Name"] == brand]
    if df.shape[0] > 0:
        return df.to_numpy()[0][1]
    else:
        return f"{brand} not in database"
def delete_image(request):
    
    if request.method=='POST':

        if 'image_url' in request.session:
            image_path = os.path.join(settings.MEDIA_ROOT, request.session['image_url'])
            if os.path.exists(image_path):
                os.remove(image_path)
            del request.session['image_url']
    return redirect('upload_picture')