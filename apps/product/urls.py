from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:product_slug>/product_cart', views.product_cart, name='product'),
    path('<slug:category_slug>/<slug:product_slug>/product_list', views.product_list, name='product'),
    path('<slug:category_slug>/', views.category, name='category')
]