from django.urls import path
from .views import CustomerListView, CustomerSearchNameView

urlpatterns = [
    path('', CustomerListView.as_view()),
    path('<str:name>/', CustomerSearchNameView.as_view())
]