from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SneakersViewSet, BrandViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'sneakers', SneakersViewSet, basename='api_sneakers')
router.register(r'brands', BrandViewSet, basename='api_brands')
router.register(r'categories', CategoryViewSet, basename='api_categories')

urlpatterns = [
    path('', include(router.urls)),
]