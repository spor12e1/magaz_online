from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import settings
from magazin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.categories_list, name='categories_list'),
    path('categories/<int:id>/', views.products_list, name='products_list'),
    path('products/<int:id>/', views.product_description, name='product_description')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



