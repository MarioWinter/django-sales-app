from django.utils import timezone

from django.db.models.base import Model as Model
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Customer

# Create your views here.

def redirect_to_sales_view(request):
    return redirect('sales/', permanent=True)

class CustomerDetailView(DetailView):
    model = Customer
    template_name = "sales/detail.html"
    context_object_name = "customer"
    
    def get_object(self):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        return obj

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