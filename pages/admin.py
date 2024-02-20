from django.contrib import admin

from .models import Reservation, Faq, Discount, FoodMenu, Category, Contact


@admin.register(Reservation)
class ReserveAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'text']


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['discount', 'description',]


@admin.register(FoodMenu)
class FoodMenuAdmin(admin.ModelAdmin):
    list_display = ['categorie', 'name', 'amount', 'rate', 'price']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description',]


@admin.register(Contact)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']

