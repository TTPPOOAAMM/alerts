from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Sneakers, Order
from .forms import SneakersForm
from basket.forms import BasketAddProductForm 

class SneakersListView(ListView):
    model = Sneakers
    template_name = 'sneakers/sneakers_list.html'
    context_object_name = 'sneakers_list'


class SneakersDetailView(DetailView):
    model = Sneakers
    template_name = 'sneakers/sneakers_detail.html'
    context_object_name = 'sneaker'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddProductForm() 
        return context


class SneakersCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Sneakers
    form_class = SneakersForm
    template_name = 'sneakers/sneakers_form.html'
    success_url = reverse_lazy('sneakers_list')
    permission_required = 'shop.add_sneakers' 


class SneakersUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Sneakers
    form_class = SneakersForm
    template_name = 'sneakers/sneakers_form.html'
    success_url = reverse_lazy('sneakers_list')
    permission_required = 'shop.change_sneakers'


class SneakersDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Sneakers
    template_name = 'sneakers/sneakers_confirm_delete.html'
    success_url = reverse_lazy('sneakers_list')
    permission_required = 'shop.delete_sneakers' 


class UserOrdersListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'sneakers/user_orders.html'
    context_object_name = 'orders_list'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-date_create')