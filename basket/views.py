from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages

from shop.models import Sneakers, Pos_order
from .basket import Basket
from .forms import BasketAddProductForm, OrderForm, RegistrationForm, LoginForm


def basket_detail(request):
    basket = Basket(request)  
    return render(request, 'basket/detail.html', {'basket': basket})  


@require_POST
def basket_add(request, product_id):
    basket = Basket(request)  
    product = get_object_or_404(Sneakers, pk=product_id)  
    form = BasketAddProductForm(request.POST)  
    if form.is_valid():
        basket.add(product=product,
                   count=form.cleaned_data['count'],
                   update_count=form.cleaned_data['reload'])  
    return redirect('basket:basket_detail')  


def basket_remove(request, product_id):
    basket = Basket(request)  
    product = get_object_or_404(Sneakers, pk=product_id)  
    basket.remove(product)  
    return redirect('basket:basket_detail')  


def basket_clear(request):
    basket = Basket(request)  
    basket.clear()  
    return redirect('basket:basket_detail')  


def basket_quantity_toggle(request, product_id, action):
    basket = Basket(request)
    product = get_object_or_404(Sneakers, pk=product_id)
    
    current_count = basket.basket.get(str(product_id), {}).get('count', 0)
    
    if action == 'add':
        basket.add(product=product, count=1, update_count=False)
    elif action == 'reduce':
        if current_count > 1:
            basket.add(product=product, count=current_count - 1, update_count=True)
        else:
            basket.remove(product)
            
    return redirect('basket:basket_detail')


@login_required  
def open_order(request):
    context = {'form_order': OrderForm()}  
    return render(request, 'basket/order_form.html', context)  


@login_required  
def basket_buy(request):
    basket = Basket(request)  
    if len(basket) <= 0:  
        return redirect('sneakers_list')  
        
    if request.method == 'POST':
        form = OrderForm(request.POST)  
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user 
            order.total_price = basket.get_total_price()  
            order.save()
            
            for item in basket:  
                Pos_order.objects.create(
                    order=order,
                    sneakers=item['product'],
                    count=item['count'],
                    discount=0
                )  
                
            basket.clear()  
            messages.success(request, 'Заказ успешно оформлен!')
            return redirect('user_orders')
    return redirect('basket:open_order')

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)  
        if form.is_valid():
            login(request, form.get_user())  
            return redirect('sneakers_list')  
    else:
        form = LoginForm()  
    return render(request, 'basket/login.html', {'form': form})  


def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)  
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            return redirect('sneakers_list')  
    else:
        form = RegistrationForm()  
    return render(request, 'basket/registration.html', {'form': form})  


def logout_user(request):
    logout(request)  
    return redirect('sneakers_list')  