from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from .models import Customer

# Create your views here.

def redirect_to_sales_view(request):
    return redirect('sales/', permanent=True)

class CustomerListView(ListView):
    model = Customer
    #queryset = Customer.objects.all()
    #queryset = Customer.objects.filter(first_name__icontains="John")
    template_name = "sales/list.html"
    context_object_name = "customers"
    paginate_by = 3
    
class CustomerSearchNameView(CustomerListView):
    def get_queryset(self):
        name = self.kwargs.get("name")
        return Customer.objects.filter(first_name__icontains=name)