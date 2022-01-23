from django.shortcuts import render
from gallery.models import Gallery, Image

# Create your views here.
def gallery(request, gallery_name):
    """View function for gallery of site"""
    # load all images in gallery as context
    gallery = Gallery.objects.get(gallery_name=gallery_name)

    context = {
        images: gallery.image_set.all(),
    }
    return 