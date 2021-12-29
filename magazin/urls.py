from django.urls import include, path
from rest_framework import routers
from magazin import viewsets


router = routers.DefaultRouter()
router.register('products', viewsets.ProductViewSet)
router.register('categories', viewsets.CategoryViewSet)
router.register('itemimage', viewsets.ItemImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.categories_list, name='categories_list'),
    path('categories/<int:id>/', views.products_list, name='products_list'),
    path('products/<int:id>/', views.product_description, name='product_description')
]
