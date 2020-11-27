from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/',views.category, name='category'),
    path('<int:id>/', views.product_details, name = 'product_details'),
	path('category/<int:id>/', views.category_items, name = 'category_items')
]