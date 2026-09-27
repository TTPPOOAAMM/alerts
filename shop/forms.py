from django import forms
from .models import Sneakers

class SneakersForm(forms.ModelForm):
    class Meta:
        model = Sneakers
        fields = ['name', 'description', 'price', 'size', 'color', 'photo', 'is_exists', 'brand', 'category']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например: Air Max'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Опишите преимущества модели...'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'size': forms.NumberInput(attrs={'class': 'form-control', 'min': 30, 'max': 50}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например: Черно-белый'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'is_exists': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }