from django.urls import path

from .views import home_page_view, about_page_view, chefs_page_view, faq_page_view, food_menu_page_view, reservation_page_view, contact_page_view


urlpatterns = [
    path('home/', home_page_view, name='home'),
    path('about/', about_page_view, name='about'),
    path('chefs/', chefs_page_view, name='chefs'),
    path('faq/', faq_page_view, name='faq'),
    path('menu/', food_menu_page_view, name='food_menu'),
    path('reservation/', reservation_page_view, name='reservation'),
    path('contact/', contact_page_view, name='contact'),
]