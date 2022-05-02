from django.contrib import admin

# Register your models here.
from Softuni_Web_Framework.main.models import Item


@admin.register(Item)
class ItemRegister(admin.ModelAdmin):
    pass
