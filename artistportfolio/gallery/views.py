from django.shortcuts import render
from gallery.models import Gallery, Image
from django.http import HttpResponse

# Create your views here.
# def gallery(request, gallery_name):
#     return HttpResponse(f'gallery: {galley_name}')


def gallery(request, gallery_name):
    """View function for gallery of site"""
    # load all images in gallery as context
    gallery = Gallery.objects.get(gallery_name=gallery_name)
    
    images = gallery.image_set.all()

    context = {
        'gallery_name': gallery_name,
        'images': images
    }

    return render(request, 'gallery.html', context)
    