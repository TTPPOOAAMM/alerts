from rest_framework import serializers
from shop.models import Sneakers, Brand, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'country']


class SneakersSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    
    class Meta:
        model = Sneakers
        fields = [
            'id', 'name', 'description', 'price', 'size', 
            'color', 'photo', 'create_date', 'is_exists', 
            'brand', 'brand_name', 'category'
        ]
        
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Цена должна быть больше нуля.")
        return value