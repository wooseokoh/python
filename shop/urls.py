from django.urls import path
from .views import *
# namespace 사용
app_name = 'shop'

urlpatterns = [
    path('',product_in_category,name='product_all'), # 루트일때 함수(product_in_category)가 호출되고 카테고리 지정여부에 의해 화면이 결정됨
    path('<slug:category_slug>/', product_in_category, name='product_in_category'),
    path('<int:id>/<product_slug>/', product_detail, name='product_detail'),
]
