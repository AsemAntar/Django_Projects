from django.contrib import admin
from .models import Pharmacy, Pharmacist, Guest


admin.site.register(Pharmacy)
admin.site.register(Pharmacist)
admin.site.register(Guest)
