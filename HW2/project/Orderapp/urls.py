from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from .views import client_orders_content, client_orders_for_period, product_form

urlpatterns = [
path('client_orders_content/<int:client_id>/', client_orders_content, name='client_orders_content'),
path('client_orders_for_period/<int:client_id>/<slug:period>', client_orders_for_period, name='client_orders_for_period'),
path('add_product/', product_form, name='product_form'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)