from django.contrib import admin
from sales.models import Bill, Customer, Order, Product, Producttype

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_filter=["first_name", "last_name", "newsletter_abo"]
    list_display=["first_name", "last_name", "account", "newsletter_abo", "email_address"]
    search_fields=["first_name", "last_name", "newsletter_abo"]
    fieldsets = [
        (
            None,
            {
                "fields": ["first_name", "last_name", "email_address"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["newsletter_abo", "account"],
            },
        ),
    ]
    

class ProductAdmin(admin.ModelAdmin):
    list_filter=["name", "price"]
    list_display=["name", "price"]
    search_fields=["name"]
    
    
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Bill)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Producttype)