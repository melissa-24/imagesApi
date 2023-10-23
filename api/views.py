from django.http import JsonResponse
from api.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


@api_view(['GET'])
def index(request):
    try:
        apiStatus = {
            "API Status": "Running"
        }
        return Response(apiStatus, status=status.HTTP_200_OK)
    except:
        apiStatus = {
            "API Status": "Error"
        }
        return Response(apiStatus, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def allCategories(request):
    try:
        categories = Category.objects.all().values()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Category.DoesNotExist:
        data = []
        return Response(data, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def allSubCategories(request):
    try:
        subCategories = SubCategory.objects.all().values()
        serializer = SubCategorySerializer(subCategories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except SubCategory.DoesNotExist:
        data = []
        return Response(data, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def allMediums(request):
    try:
        mediums = Medium.objects.all().values()
        serializer = MediumSerializer(mediums, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Medium.DoesNotExist:
        data = []
        return Response(data, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def allImages(request):
    try:
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        print('images', images, 'serializer.data', serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Image.DoesNotExist:
        data = []
        return Response(data, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def oneImage(request, image_id):
    try:
        images = Image.objects.get(id=image_id)
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Image.DoesNotExist:
        data = []
        return Response(data, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def byCategory(request, category_id):
    try:
        images = Image.objects.filter(category_id=category_id)
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Image.DoesNotExist:
        data = []
        return Response(data, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def byCategorySubCategory(request, category_id, subCategory_id):
    pass

@api_view(['GET'])
def byCategorySubCategoryMedium(request, category_id, subCategory_id, medium):
    pass




# category, category/sub, category/medium
# category/sub, category/sub/medium
# medium, medium/category, medium/category/sub