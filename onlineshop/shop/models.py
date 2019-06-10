from django.db import models
from django.urls import reverse
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True) # db 인덱스 사용(검색시 속도증가)
    meta_description = models.TextField(blank=True) # 제품에 대한 설명
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True) # 특수기호가 들어간 스트링
    class Meta:
        ordering = ['name'] # 이름으로 정렬
        verbose_name = 'category'
        verbose_name_plural = 'categories' # 관리자 모드
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_in_category', args=[self.slug])
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products') # null이 올수있다.
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True) # 아무것도 없어도 되는 필드, from에서 값을 받아올때 -> 공백처리를 해준다.
    meta_description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2) # 10억까지 표기가능
    stock = models.PositiveIntegerField()

    available_display = models.BooleanField('Display', default=True) # 관리자모드에서 표현 될때 모두 보여줌, 상품품절시 보여지는 것들
    available_order = models.BooleanField('Order', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created'] # 내리차순(최신것이 밑으로 내려감)
        index_together = [['id','slug']] # 두개의 기본값을 가지고 찾는 변수
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug]) # 상품을 보려면 기본값 두개가 들어가야함