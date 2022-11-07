from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('apps.core.pages.urls')),
    path('cart/', include('apps.cart.pages.urls', namespace='cart')),
    path('orders/', include('apps.orders.pages.urls', namespace='orders')),
    path('', include('apps.shop.pages.urls', namespace='shop')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    