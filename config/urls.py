
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('accounts/', include('allauth.urls')), # 눈에는 안보이고 내부적으로 인증을 받을 수 있음
    path('cart',include('cart.urls')),
]
