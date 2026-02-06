from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),   # 👈 ROOT URL
    path('index/', views.index),
    path('about/', include('app_wedding.urls')),
]
