from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_detail, name='list'),
    # path('success/', views.success, name='success')
]