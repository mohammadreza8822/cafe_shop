from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse

from .forms import ReserveForm, FaqForm, ContactForm
from .models import FoodMenu, Category


def home_page_view(request):
    return render(request, 'pages/home.html')


def about_page_view(request):
    return render(request, 'pages/about.html') 


def chefs_page_view(request):
    return render(request, 'pages/chefs.html')


def faq_page_view(request):
    if request.method == "POST":
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = FaqForm()
        
    return render(request, 'pages/faq.html', {'form': form})


def food_menu_page_view(request):
    brakefast = FoodMenu.objects.filter(categorie__title__icontains=Category.BRAKEFAST)
    lunch = FoodMenu.objects.filter(categorie__title__icontains=Category.LUNCH)
    dinner = FoodMenu.objects.filter(categorie__title__icontains=Category.DINNER)
    rate = FoodMenu.rate
    return render(request, 'pages/food_menu.html', {'brakefast': brakefast,
                                                    'lunch':lunch,
                                                    'dinner':dinner,
                                                    'rate': rate})


def reservation_page_view(request):
    if request.method == "POST":
        form = ReserveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = ReserveForm()

    return render(request, 'pages/reservation.html', {'form':form})

    
def contact_page_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form':form})
