from django.contrib import admin
from .models import *
# admin.ModelAdmin 을 상속 받으면 admin 페이지를 받음
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug'] # 보여주고 싶은 항목
    prepopulated_fields = {'slug' : ('name',)} # 이름을 넣었을때 공백이 있으면 _ 을 넣어줌

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available_display', 'available_order', 'created',
                    'updated']
    list_filter = ['available_display', 'created', 'updated', 'category']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'stock', 'available_display', 'available_order']

admin.site.register(Category, CategoryAdmin) # admin은 화면을 그 클래스
admin.site.register(Product, ProductAdmin)