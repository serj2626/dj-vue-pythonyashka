from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('studies.urls')),
]
