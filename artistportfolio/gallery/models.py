from django.db import models

class Gallery(models.Model):
    """Model representing a gallery of images"""
    project_title = models.CharField()

    def __str__(self):
        """string for representing the Model object"""
        return self.project_title

        
class Image(models.Model):
    """Model representing a particular image/work of art"""
    photo = models.ImageField()
    title = models.CharField
    gallery = models.ForeignKey('Gallery', on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object"""
        return self.title

