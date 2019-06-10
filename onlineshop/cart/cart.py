# 카트 기능을 클래스로 묶어버리는 모듈
from django.conf import settings

from decimal import Decimal
from shop.models import Product


class Cart(object):
    def __init__(self, request): # 세션으로 settings.py에 넣은거 가져오기
        self.session = request.session # 요청을 받은 세션을 가지고 오는 부품을 얻을수가 있음 (세션은 만들어져있음)

        # CART_ID Key를 가진 세션이 있는지 체크
        cart = self.session.get(settings.CART_ID) # 불러온 값이 있으면 가지고 와서 cart에 넣음
        loginId = self.session.get(settings.LOGIN_SESSION_ID) # 불러온 값이 있으면 가지고와서 loginid에 저장

        print('start_value:', settings.START + 1)
        print('login-id', settings.LOGIN_SESSION_ID)
        # 세션이 없으면, 딕셔너리를 만들어주어야 함.
        if not cart:
            cart = self.session[settings.CART_ID] = {}

        # 세션이 있으면, 딕셔너리를 가지고 옴.
        self.cart = cart

    def __len__(self): # cart의 길이 = 몇개의 값이 들어가 있는지 자동을 세어줌
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self): # 반복자
        product_ids = self.cart.keys() # 키를 한번에 다 가져옴
        # id__in = id 중 장바구니_ids에 있으면 모두 필터링해서 가져온다
        products = Product.objects.filter(id__in=product_ids) # 장바구긴에 담긴 제품의 정보를 다 가져옴

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']

            yield item

    def add(self, product, quantity=1, is_update=False):
        product_id = str(product.id)
        if product_id not in self.cart: # 카트에 물건이 있는지 확인 없으면 추가
            self.cart[product_id] = {'quantity':0, 'price':str(product.price)}

        if is_update:
            self.cart[product_id]['quantity'] = quantity # 개수 업데이트
        else:
            self.cart[product_id]['quantity'] += quantity # 기존에 있던것에 추가

        self.save()

    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True

    def remove(self, product): # 하나씩 지우는 기능
        product_id = str(product.id)
        if product_id in self.cart:
            del(self.cart[product_id])
            self.save()

    def clear(self):
        self.session[settings.CART_ID] = {}
        self.session.modified = True

    def get_product_total(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return self.get_product_total()








