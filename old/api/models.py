from django.db import models
from django.db.models.deletion import CASCADE

class Category(models.Model):
    category = models.CharField(max_length=255)
    def __str__(self):
        return self.category

class SubCategory(models.Model):
    subCategory = models.CharField(max_length=255)
    def __str__(self):
        return self.subCategory

class Medium(models.Model):
    medium = models.CharField(max_length=255)
    def __str__(self):
        return self.medium

class UploadImage(models.Model):
    fileName = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images")
    extension = models.CharField(max_length=10)
    def __str__(self):
        return self.fileName

class ImageLink(models.Model):
    fileName = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    extension = models.CharField(max_length=10)
    def __str__(self):
        return self.fileName

class Image(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='theCategory', on_delete=CASCADE, blank=True, null=True)
    subCategory = models.ForeignKey(SubCategory, related_name='theSubCategory', on_delete=CASCADE, blank=True, null=True)
    medium = models.ForeignKey(Medium, related_name='theMedium', on_delete=CASCADE, blank=True, null=True)
    fileName = models.ForeignKey(UploadImage, related_name='theFileName', on_delete=CASCADE, blank=True, null=True)
    linkName = models.ForeignKey(ImageLink, related_name='theLinkName', on_delete=CASCADE, blank=True, null=True)
    birthday = models.CharField(max_length=255, blank=True, null=True)
    spouse = models.CharField(max_length=255, blank=True, null=True)
    voicedBy = models.CharField(max_length=255, blank=True, null=True)
    tvShow = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.name
