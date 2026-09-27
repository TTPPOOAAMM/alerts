from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from shop.models import Order

class BasketAddProductForm(forms.Form):
    count = forms.IntegerField(min_value=1, initial=1, label='Количество',
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))
    reload = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput) 


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['buyer_firstname', 'buyer_name', 'buyer_surname', 'comment', 'delivery_address', 'delivery_type'] 
        widgets = {
            'buyer_firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'buyer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'buyer_surname': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
            'delivery_address': forms.TextInput(attrs={'class': 'form-control'}),
            'delivery_type': forms.Select(attrs={'class': 'form-control'}),
        }


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))