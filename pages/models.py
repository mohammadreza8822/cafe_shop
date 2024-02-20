from django.db import models

from ckeditor.fields import RichTextField

class Category(models.Model):
    BRAKEFAST = 'brakefast'
    LUNCH = 'lunch'
    DINNER = 'dinner'
    CATEGORY = (
        ( BRAKEFAST, 'brakefast'),
        ( LUNCH, 'lunch'),
        ( DINNER, 'dinner')
    )
    title = models.CharField(max_length=255, choices=CATEGORY)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class Discount(models.Model):
    discount = models.FloatField()
    description = models.CharField(max_length=255)


class FoodMenu(models.Model):
    RATE = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    )
    categorie = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    amount = models.CharField(max_length=100)
    rate = models.IntegerField(choices=RATE)
    slug = models.SlugField()
    description = RichTextField()
    price = models.IntegerField()
    discounts = models.ManyToManyField(Discount, blank=True)
    image = models.ImageField(upload_to='foods/', blank=True)
    inventory = models.IntegerField()

    def __str__(self) -> str:
        return self.categorie.title



class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    date = models.DateField()
    people = models.IntegerField()
    time = models.IntegerField()



class Faq(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField(max_length=300)

    
class Contact(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
