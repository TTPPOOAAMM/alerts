from django.urls import path
from .views import (
    SneakersListView, SneakersDetailView, 
    SneakersCreateView, SneakersUpdateView, SneakersDeleteView,
    UserOrdersListView
)

urlpatterns = [
    path('sneakers/', SneakersListView.as_view(), name='sneakers_list'),
    path('sneakers/<int:pk>/', SneakersDetailView.as_view(), name='sneakers_detail'),
    path('sneakers/create/', SneakersCreateView.as_view(), name='sneakers_create'),
    path('sneakers/<int:pk>/update/', SneakersUpdateView.as_view(), name='sneakers_update'),
    path('sneakers/<int:pk>/delete/', SneakersDeleteView.as_view(), name='sneakers_delete'),
    path('my-orders/', UserOrdersListView.as_view(), name='user_orders'),
]