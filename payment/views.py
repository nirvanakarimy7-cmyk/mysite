from django.shortcuts import render,redirect,get_object_or_404
from cart.cart import Cart
from.forms import shippingform
from.models import shippingdress,order,orderitem
from django.contrib import messages
from shop.models import Product,Profile
from django.contrib.auth.models import User



def payment_success(request):
    return render(request,'payment/payment_success.html',{})

def checkout(request):
    cart=Cart(request)
    cart_products=cart.get_prods()
    quantities=cart.get_quants()
    total=cart.get_total()
     
    if request.user.is_authenticated:
        shipping_user=shippingdress.objects.get(user__id=request.user.id)
        shipping_form = shippingform(request.POST or None,instance=shipping_user)
        return render(request, 'checkout.html',
                  {'cart_products':cart_products,
                                        'quantities':quantities,'total':total,
                                            'shipping_form':shipping_form})
    else:
        shipping_form = shippingform(request.POST or None)
        return render(request, 'checkout.html',
                  {'cart_products':cart_products,
                                        'quantities':quantities,'total':total,
                                            'shipping_form':shipping_form})
def confirm_order(request):
    if request.POST:
        cart=Cart(request)
        cart_products=cart.get_prods()
        quantities=cart.get_quants()
        total=cart.get_total()

        user_shipping=request.POST
        request.session['user_shipping']=user_shipping

        return render(request,'payment/confirm_order.html',
                  {'cart_products':cart_products,
                                        'quantities':quantities,'total':total,
                                            'shipping_info':user_shipping})
        
    else:
        messages.success(request,"you cant access to this page")
        return redirect('home')

    #return render(request,'payment/confirm_order.html',{})

def process_order(request):
    if request.POST:
        cart=Cart(request)
        cart_products=cart.get_prods()
        quantities=cart.get_quants()
        total=cart.get_total()

        user_shipping=request.session.get('user_shipping')

        full_name=user_shipping['shipping_fullname']
        email=user_shipping['shipping_email']
        full_address=f"{user_shipping['shipping_address1']}\n{'shipping_address2'}\n{'shipping_city'}\n{'shipping_state'}\n{'shipping_zipcode'}\n{'shipping_country'}\n"
        
        if request.user.is_authenticated:
            user=request.user
            new_order=order(
                user=user,
                full_name=full_name,
                email=email,
                shippingdress=full_address,
                amount_paid=total
            )
            new_order.save()

            odr=get_object_or_404(order,id=new_order.pk)
            for product in cart_products:
                prod=get_object_or_404(Product,id=product.id)

                if product.is_sale:
                    price=product.sale_price
                else:
                    price=product.price
                
                for k,v in quantities.items():
                    if int(k)==product.id:
                        new_item = orderitem(
                            order=odr,
                            product=prod,
                            price=price,
                            quantities=v,
                            user=user
                        )
                        new_item.save()
            messages.success(request,"it is accepted")

            for key in list(request.session.keys()):
                if key == 'session_key':
                    del request.session[key]
            cu= Profile.objects,filter(user__id=request.user.id)
            cu.update(old_cart="")

            return redirect('home')
        else:
            new_order=order(
                full_name=full_name,
                email=email,
                shippingdress=full_address,
                amount_paid=total
            )
            new_order.save()
            for product in cart_products:
                prod=get_object_or_404(Product,id=product.id)

                if product.is_sale:
                    price=product.sale_price
                else:
                    price=product.price
                
                for k,v in quantities.items():
                    if int(k)==product.id:
                        new_item = orderitem(
                            order=odr,
                            product=prod,
                            price=price,
                            quantities=v,
                        )
                        new_item.save()
            for key in list(request.session.keys()):
                if key == 'session_key':
                    del request.session[key]
            messages.success(request,"it is accepted")
            return redirect('home')
    else:
        messages.success(request,"you cant access to this page")
        return redirect('home')
