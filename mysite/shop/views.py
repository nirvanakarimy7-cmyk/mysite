from django.shortcuts import render ,redirect
from .models import Product,Category,Profile
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import signupform,updateuserform,updatepass,updateuserInfo
from django.db.models import Q
import json
from cart.cart import Cart

from payment.forms import shippingform
from payment.models import shippingdress,order,orderitem


def order_details(request,pk):
    if request.user.is_authenticated:
            Order=order.objects.get(id=pk)
            items=orderitem.objects.filter(order=pk)

            context={
                'order':order,
                'items':items
            }
            return render(request,'order_details.html',context)
    else:
        messages.success(request,'you cant access to this page')
        return redirect ('home')


def user_orders(request):
    if request.user.is_authenticated:
        delivered_orders=order.objects.filter(user=request.user,status='delivered')
        other_orders=order.objects.filter(user=request.user).exclude(status='delivered')

        context={
          'delivered': delivered_orders,
          'other': other_orders
        }
        return render(request,'orders.html',context)
    else:
        messages.success(request,'you cant access to this page')
        return redirect ('home')

def search(request):
    if request.method=='POST':
        searched=request.POST['searched']
        searched=Product.objects.filter(Q(name__icontains=searched)| Q(description__icontains=searched))
        
        if not searched:
            messages.success(request,"it's not found")
            return render(request,'search.html',{})
        else:
            return render(request,'search.html',{'searched':searched})
    return render(request,'search.html',{})

def update_info(request):
    if request.user.is_authenticated:
        current_user=Profile.objects.get_or_create(user__id=request.user.id)
        shipping_user=shippingdress.objects.get_or_create(user__id=request.user.id)

        form=updateuserInfo(request.POST or None,instance=current_user)
        shipping_form =shipping_form(request.POST or None,instance=shipping_user)

        if form.is_valid() or shipping_form.is_valid():

            form.save()
            shipping_form.save()
            messages.success(request,"information are edited")
            return redirect('home')
        return render(request,'update_info.html',{'form':form , 'shipping_form':shipping_form})
    else:
        messages.success(request,"you must login")
        return redirect('home')  
    

def category_summary(request):
    all_cat=Category.objects.all()
    return render(request,'category_summary.html',{'category':all_cat})

def helloword(request):
    all_products=Product.objects.all()
    return render(request,'index.html',{'products': all_products})

def about(request):
    return render(request, 'about.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            current_user = Profile.objects.get(user__id = request.user.id)
            saved_cart =current_user.old_cart

            if saved_cart:
                converted_cart =json.loads(saved_cart)

                cart=Cart(request)
                for key,value in converted_cart.items():
                    cart.db_add(product=key,quantity=value)

            messages.success(request, "You logged in successfully")
            return redirect("home")

        else:
            messages.success(request, "Invalid username or password")
            return redirect("home")

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,(" you logedout "))
    return redirect("home")

def signup_user(request):
    if request.method == "POST":
        form = signupform(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(
                request,
                username=username,
                password=password
            )

            login(request, user)
            messages.success(request, "your account is created")
            return redirect("update_info")

        else:
            print(form.errors)
            messages.error(request, form.errors)

            return render(request, 'signup.html', {'form': form})

    else:
        form = signupform()
        return render(request, 'signup.html', {'form': form})

def update_user(request):
    if request.user.is_authenticated:
        current_user=User.objects.get(id=request.user.id)
        user_form=updateuserform(request.POST or None,instance=current_user)

        if user_form.is_valid():
            user_form.save()
            login(request,current_user)
            messages.success(request,"it's edited")
            return redirect('home')
        return render(request,'update_user.html',{'user_form':user_form})
    else:
        messages.success(request,"you must login")
        return redirect('home')  

def update_password(request):
    if request.user.is_authenticated:
        current_user=request.user
        if request.method =='POST':
            form=updatepass(current_user,request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'your password saved successfully')
                login(request,current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request,error)
                return redirect('update_password')
        else:
            form=updatepass(current_user)
            return render(request,'update_password.html',{'form':form})
    else:
        messages.success(request,'you must login')
        return redirect('home')

   

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})

def category(request, cat):
    cat = cat.replace("-", " ")

    try:
        category = Category.objects.get(name=cat)
        products = Product.objects.filter(Category=category)

        return render(
            request,
            'category.html',
            {
                'products': products,
                'category': category
            }
        )
    except Category.DoesNotExist:
        messages.success(request, "Category is not found")
        return redirect("home")