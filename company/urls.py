from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('management/', views.management, name='management'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('contact/', views.contacts),

    path('news/<path:rest>', views.news),
    path('management/<path:rest>', views.management),
    path('about/<path:rest>', views.about),
    path('contacts/<path:rest>', views.contacts),
    path('contact/<path:rest>', views.contacts),
]
