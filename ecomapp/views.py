from django.shortcuts import render, redirect
from .models import *
from django.views.generic.base import TemplateView
from .forms import *
from django.http import JsonResponse
import json
# Create your views here.

class HomeView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


def LogIn(request):
    form = loginform()
    context = {'form' : form}
    return render(request, 'login.html', context)


class AboutView(TemplateView):

    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context

class ShoeView(TemplateView):
    template_name = 'shoestore.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Category.objects.filter(title='Shoe Collection')
        list_shoes = 0
        for cat in products:
            list_shoes = cat.product_set.all()  
        context['products'] = list_shoes
        return context

class MenView(TemplateView):
    template_name = 'menstore.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Category.objects.filter(title='Men Fashion')
        men_cloths = 0
        for cat in products:
            men_cloths = cat.product_set.all()  
        context['products'] = men_cloths
        return context
        

class WomenView(TemplateView):
    template_name = 'womenstore.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Category.objects.filter(title='Women Fashion')
        women_cloths = 0
        for cat in products:
            women_cloths = cat.product_set.all()  
        context['products'] = women_cloths
        return context


class ProductView(TemplateView):                                # we can give same with function by giving parameters like
    template_name = 'productview.html'                          # def ProductView(request, parameters)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        product = Product.objects.get(slug=slug)
        context['product'] = product
        return context


def AddToCart(request):
    data = json.loads(request.body)                 # grab data from backend
    product_id = data['productId']
    print('See productId :', product_id)
    #get product
    product_obj = Product.objects.get(id=product_id)

    # check if cart exists
    cart_id =request.session.get('cart_id', None)
    #request.session.flush()                            #this line delete existing sessions
    print('this is session :', cart_id)
    if cart_id:
        cart_obj = Cart.objects.get(id=cart_id)
        product_in_cart = cart_obj.cartitem_set.filter(product=product_obj)
        # item already in cart
        if product_in_cart.exists():
            cartitem = product_in_cart.last()
            cartitem.quantity += 1
            cartitem.total += product_obj.price
            cartitem.save()
            cart_obj.total += product_obj.price
            cart_obj.save()

        else:
            cartitem = CartItem.objects.create(
                cart=cart_obj, product=product_obj, price=product_obj.price, quantity=1, total=product_obj.price
            )
            cart_obj.total += product_obj.price
            cart_obj.save()
        
    else:
        cart_obj = Cart.objects.create(total=0)
        request.session['cart_id'] = cart_obj.id
        cartitem = CartItem.objects.create(
                cart=cart_obj, product=product_obj, price=product_obj.price, quantity=1, total=product_obj.price
            )
        cart_obj.total += product_obj.price
        cart_obj.save()
        
    return JsonResponse('Item was added', safe=False)


def CartView(request):

    context = {}

    return render(request, 'cart.html', context)


# class CartView(TemplateView):
#     template_name = 'cart.html'

