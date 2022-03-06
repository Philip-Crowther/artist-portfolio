from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

class Gallery(models.Model):
    """Model representing a gallery of images"""
    gallery_name = models.CharField(max_length=40)

    class Meta:
        verbose_name='Gallery'
        verbose_name_plural='Galleries'

    def __str__(self):
        """string for representing the Model object"""
        return self.gallery_name

        
class Image(models.Model):
    """Model representing a particular image/work of art"""
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=30)
    gallery = models.ForeignKey('Gallery', on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object"""
        return self.title

