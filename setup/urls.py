from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('v1/auth/', include('apps.authentication.urls')),
    path('v1/products/', include('apps.products.urls')),
    path('admin/', admin.site.urls),
]
