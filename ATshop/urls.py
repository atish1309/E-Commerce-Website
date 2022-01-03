
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vendors/', include('apps.vendor.urls')),
    path('accounts/', include('allauth.urls'),name='google'),
    path('cart/', include('apps.cart.urls')),
    path('shop_list/', include('apps.shop_list.urls')),
    path('users/',include('apps.users.urls')),
    path('', include('apps.core.urls')),
    path('', include('apps.product.urls')),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
