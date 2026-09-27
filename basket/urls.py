from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.basket_detail, name='basket_detail'),
    path('add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('remove/<int:product_id>/', views.basket_remove, name='basket_remove'),
    path('clear/', views.basket_clear, name='basket_clear'),
    path('quantity/<int:product_id>/<str:action>/', views.basket_quantity_toggle, name='basket_quantity_toggle'),
    path('create-order/', views.open_order, name='open_order'),
    path('buy/', views.basket_buy, name='basket_buy'),
    
    path('login/', views.login_user, name='login_page'),
    path('registration/', views.registration_user, name='registration_page'),
    path('logout/', views.logout_user, name='logout_page'),
]