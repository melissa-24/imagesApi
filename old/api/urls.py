from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('categories/', views.allCategories),
    path('subCategories/', views.allSubCategories),
    path('mediums/', views.allMediums),
    path('images/', views.allImages),
    path('images/<int:image_id>/view/', views.oneImage),
    path('images/<int:category_id>/viewAllImages/', views.byCategory),
    path('images/<int:category_id>/<int:subCategory_id>/viewAllImages/', views.byCategorySubCategory),
    path('images/<int:category_id>/<int:medium_id>/viewAllImages/', views.byCategoryMedium),
     path('images/<int:category_id>/<int:subCategory_id>/<int:medium_id>/viewAllImages/', views.byCategorySubCategoryMedium),
    path('images/<int:medium_id>/viewAllImages/', views.byMedium),
    path('images/<int:medium_id>/<int:category_id>/viewAllImages/', views.byMediumCategory),
    path('images/<int:medium_id>/<int:category_id>/<int:subCategory_id>/viewAllImages/', views.byMediumCategorySubCategory),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)