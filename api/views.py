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
        images = Image.objects.all().values()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Image.DoesNotExist:
        data = []
        return Response(data, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def imagesByCategory(request, category_id):
    try:
        images = Image.objects.filter(category_id=category_id)
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Image.DoesNotExist:
        data = []
        return Response(data, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def imagesByMedium():
    pass

@api_view(['GET'])
def imagesByMediumCategory():
    pass

@api_view(['GET'])
def oneImage():
    pass

@api_view(['GET'])
def oneCategory():
    pass

@api_view(['GET'])
def oneMedium():
    pass

@api_view(['GET'])
def randomImage():
    pass

@api_view(['GET'])
def randomImageByCategory():
    pass

@api_view(['GET'])
def randomImageByMedium():
    pass

@api_view(['GET'])
def randomImageByCategoryMedium():
    pass

@api_view(['GET'])
def randomNumImage():
    pass

@api_view(['GET'])
def randomNumImageByCategory():
    pass

@api_view(['GET'])
def randomNumImageByMedium():
    pass

@api_view(['GET'])
def radnomNumImageByCategoryMedium():
    pass