from django.urls import path
from .views import *
# namespace 사용
app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>', add, name='product_add'),
    path('', detail, name='detail'),
    path('remove/<product_id>', remove, name='product_remove'),
]
