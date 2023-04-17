from django.contrib import admin
from .models import ForeignDrugUser, ForeignDrugUserNation

admin.site.register(ForeignDrugUser,ForeignDrugUserNation)

# Register your models here.
