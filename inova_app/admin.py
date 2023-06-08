from django.contrib import admin
from .models import Customer, LoyaltyProgram, Purchase, LoyaltyPoint

admin.site.register(Customer)
admin.site.register(LoyaltyProgram)
admin.site.register(Purchase)
admin.site.register(LoyaltyPoint)