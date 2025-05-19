from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin
    path('', include('crud_app.urls')),  # Include the urls from your app
]
