from django.contrib import admin
from . models import Product, Customer, Cart, Payment,OrderPlaced
# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_dispaly = ['id','title','discount_price','category','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_dispaly = ['id','user','locality','city','zipcode']

@admin.register(Cart)
class CustomerModelAdmin(admin.ModelAdmin):
    list_dispaly = ['id','user','product','quantity']  

@admin.register(OrderPlaced)
class CustomerModelAdmin(admin.ModelAdmin):
    list_dispaly = ['id','user','customers','product','quantity','order_date','status','payment']


@admin.register(Payment)
class CustomerModelAdmin(admin.ModelAdmin):
    list_dispaly = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']          