from django.urls import path
from .views import (
    LoginView,
    VendorRegisterView,
    CustomerRegisterView,
    VendorListVIew,
    VendorProfileView,
    VendorDetailAPIView,
    CustomerListVIew,
    CustomerCountView,
    VendorCountView
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('vendor/register/', VendorRegisterView.as_view(), name='vendor-register'),
    path('customer/register/', CustomerRegisterView.as_view(), name='customer-register'),
    path('vendor/list/', VendorListVIew.as_view(), name='vendor-list'),
    path('customer/list/', CustomerListVIew.as_view(), name='customer-list'),
    path('vendor/profile/<str:token>', VendorProfileView.as_view(), name='vendor-profile'),
    path('vendor/detail/<int:id>/', VendorDetailAPIView.as_view(), name='vendor-detail'),
    path('customer/count/', CustomerCountView.as_view(), name='customer-count'),
    path('vendor/count/', VendorCountView.as_view(), name='vendor-count')
]