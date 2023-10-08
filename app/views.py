from django.shortcuts import render,redirect
from . models import Product, Customer, Cart
from django.views import View
from django.db.models import Count
from . forms import CustomerRegistrationForm , CustomerProfileForm
from django.contrib import messages

def home(request):
    return render(request, "app/home.html")

def about(request):
    return render(request,"app/about.html")
def contact(request):
    return render(request,"app/contact.html")

# def category(request,val):
#     product = Product.objects.filter(category=val)
#     return render(request,"app/category.html",locals())


class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category = val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())
    
class CategoryTitle(View):
    def get(self, request, val):
        product= Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"app/category.html",locals())

class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk = pk)
        return render(request,"app/detail.html",locals())    
    
class CustomerRegistrationView(View):
    def get(sef,request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User register successfully! ")
        else:
            messages.warning (request,"Invalid Input Data")

        return render(request, 'app/customerregistration.html',locals())

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm() 
        return render(request, 'app/profile.html',locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user = user,name=name,mobile=mobile,locality=locality,city=city,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congtratulations! Profile Save Successfullly")
        else:
            messages.warning(request,"Invalid Input Data")    
        return render(request, 'app/profile.html',locals())

def address(request):
    add = Customer.objects.filter(user = request.user)
    return render(request,'app/address.html',locals())

class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'app/updateAddress.html',locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.mobile = form.cleaned_data['mobile']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"Congratualation Profile Update Successfully")
        else:
            messages.warning(request,"Invalid Input!!")    
        return redirect("address")
    


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect("/cart")

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discount_price
        amount = amount + value

    totalamount = amount + 40    
    return render(request, 'app/addtocart.html',locals())

class checkout(View):
    def get(self,request):
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_item = Cart.objects.filter(user = user)
        famount = 0
        for p in cart_item:
            
            value = p.quantity * p.product.discount_price
            famount = famount + value
        totalamount = famount + 40    
        return render(request,'app/checkout.html',locals())
      