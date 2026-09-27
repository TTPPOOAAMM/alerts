from rest_framework import viewsets, filters
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from shop.models import Sneakers, Brand, Category
from .serializers import SneakersSerializer, BrandSerializer, CategorySerializer

class SneakersViewSet(viewsets.ModelViewSet):
    queryset = Sneakers.objects.all().order_by('-create_date')
    serializer_class = SneakersSerializer
    
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    search_fields = ['name', 'description', 'brand__name', 'color']
    
    ordering_fields = ['price', 'create_date', 'size']


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('name')
    serializer_class = BrandSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]