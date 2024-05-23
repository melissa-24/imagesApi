from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Medium)
admin.site.register(UploadImage)
admin.site.register(ImageLink)
admin.site.register(Image)

