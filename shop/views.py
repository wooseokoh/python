from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
# 모든 카테고리 출력
# 해당 카테고리 클릭시 해당 카테고리만 출력

def product_in_category(request, category_slug=None): # category_slug가 있으면 입력값을 넣어줌, category_slug없으면 전체검색, default 값지정(category_slug=None)
    # db 검색한 결과를 템플릿에 넘겨줌
    # map 형태로 만들어서 넘겨줌.

    # category없이 전체 출력
    current_category = None
    categories = Category.objects.all() # 전체출력
    products = Product.objects.filter(available_display = True)

    # category해당하는 것만 출력
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug) # objects.filter와 같은 역할
        products = products.filter(category=current_category)

    return render(request, 'shop/list.html', {
        'current_category': current_category,
        'categories': categories,
        'products': products
    })

# 제품에 대한 상세페이지 출력

from cart.forms import AddProductForm
def product_detail(request, id, product_slug=None): # 검색은 id 와 slug 값으로
    product = get_object_or_404(Product, id=id, slug=product_slug) # 값이 없다면 none을 default로 넣어줌
    add_to_cart = AddProductForm(initial={'quantity':1})
    return render(request, 'shop/detail.html', {'product': product, 'add_to_cart':add_to_cart})

























