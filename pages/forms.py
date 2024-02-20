from django.forms import ModelForm

from .models import Reservation, Faq, Contact


class ReserveForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['name','phone','email','date','people','time']
    

class FaqForm(ModelForm):
    class Meta:
        model = Faq
        fields = ['name', 'email', 'text']


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['text', 'name', 'email', 'phone']