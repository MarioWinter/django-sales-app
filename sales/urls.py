from django.urls import path
from .views import CustomerListView, CustomerSearchNameView, CustomerDetailView

urlpatterns = [
    path('', CustomerListView.as_view()),
    path('<str:name>/', CustomerSearchNameView.as_view()),
    path('customer/<int:pk>', CustomerDetailView.as_view())
]