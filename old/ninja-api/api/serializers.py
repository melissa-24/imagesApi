from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class MediumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medium
        fields = '__all__'

class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = '__all__'

class ImageLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageLink
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    
    category_name = serializers.CharField(source='category.category', read_only=True)
    subCategory_name = serializers.CharField(source='subCategory.subCategory', read_only=True)
    medium_name = serializers.CharField(source='medium.medium', read_only=True)
    fileName_image = serializers.CharField(source='fileName.image', read_only=True)
    linkName_image = serializers.CharField(source='linkName.image', read_only=True)
    fileName_imageLink = serializers.SerializerMethodField()
    fileName_name = serializers.SerializerMethodField()
    linkName_name = serializers.SerializerMethodField()

    def get_fileName_imageLink(self, obj):
        if obj.fileName:
            return f"https://ninja-api.navyladyveteran.com/media/{obj.fileName.image}"

    def get_fileName_name(self, obj):
        print('inside getfilename')
        if obj.fileName:
            print('print me more data from inside serializer',obj.fileName.fileName, obj.fileName.extension)
            return f"{obj.fileName.fileName}.{obj.fileName.extension}"
        return None
    
    def get_linkName_name(self, obj):
        print('inside getlinkname')
        if obj.linkName:
            return f"{obj.linkName.fileName}.{obj.linkName.extension}"
        return None
    
    class Meta:
        model = Image
        fields = '__all__'