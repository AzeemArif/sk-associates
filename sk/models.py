from django.db import models


class GalleryFolders(models.Model):
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class GalleryImages(models.Model):
    folder = models.ForeignKey(GalleryFolders, on_delete=models.CASCADE, related_name='folders_related_name')
    image_title = models.CharField(max_length=50)
    image_decsription = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image_title