from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .forms import AddProductForm
from .cart import *


@require_POST
def add(request, product_id):
    print('장바구니에 넣는 제품id:', product_id)
    cart = Cart(request) # 클래스의 객체 생성
    product = get_object_or_404(Product, id=product_id)
    # 유효한 값이 들어가 있는 체크
    # input에 들어간 values를 가지고 옴.
    form = AddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data # 입력값을 딕셔너리 형태로 가져옴
        cart.add(product=product, quantity=cd['quantity'], is_update=cd['is_update'])
    return redirect('cart:detail') # redirect 쪽으로 요청

def remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:detail')

def detail(request):
    cart = Cart(request)
    for product in cart:
        product['quantity_form'] = AddProductForm(initial={'quantity':product['quantity'], 'is_update':True})
    return render(request, 'cart/detail.html', {'cart':cart})

