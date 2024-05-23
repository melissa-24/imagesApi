from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_swagger.views import get_swagger_view
from core import views as app_views

schema_view = get_schema_view(
    openapi.Info(
        title="Images API",
        default_version="v1",
        description="",
        admin="http://127.0.0.1:8000/admin/",
        terms_of_service="http://127.0.0.1:8000/admin/",
        contact=openapi.Contact(email="TBD@TBD.com"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
    path('admin/', admin.site.urls),
    # path('api/', include('core.urls')),
]
