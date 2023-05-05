from django.urls import path
from .views import (
    ProductCreateAPIView,
    ProductDetailAPIView,
    # CategoryCreateAPIView,
    # CategoryListAPIView,
    CategoryDeleteAPIView,
    CategoryUpdateAPIView,
    ProductDeleteAPIView,
    ProductUpdateAPIView,
    ProductList,
    ProductSearch,
    CreateCheckoutSession,
    ProductStatistics,
    AddToCartView
)
from .models import Product
from django_filters.views import FilterView

urlpatterns = [
    path('list/', ProductList.as_view(), name='product-list'),
    # path('list/category', CategoryListAPIView.as_view(), name='category-list'),
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
    # path('create/category', CategoryCreateAPIView.as_view(), name='category-create'),
    path('<int:id>/delete/category', CategoryDeleteAPIView.as_view(), name='category-delete'),
    path('<int:id>/delete/', ProductDeleteAPIView.as_view(), name='product-delete'),
    path('<int:id>/update/category', CategoryUpdateAPIView.as_view(), name='category-delete'),
    path('<int:id>/update/', ProductUpdateAPIView.as_view(), name='product-delete'),
    path('<int:id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('search/', ProductSearch.as_view(), name='product-search'),
    path('statistics/', ProductStatistics.as_view(), name='product-statistics'),
    path('create-checkout-session/<int:id>/', CreateCheckoutSession.as_view()),
    path('cart/<int:user_id>/add/', AddToCartView.as_view(), name='add-cart'),
]