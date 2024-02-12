from django.urls import path

from .views import client_orders_content, client_orders_for_period

urlpatterns = [
path('client_orders_content/<int:client_id>/', client_orders_content, name='client_orders_content'),
path('client_orders_for_period/<int:client_id>/<slug:period>', client_orders_for_period, name='client_orders_for_period'),
]