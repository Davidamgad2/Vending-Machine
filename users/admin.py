from django.contrib import admin
from .models import Buyer,Seller,CustomUser
# Register your models here.

admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(CustomUser)