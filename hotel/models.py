from django.db import models
from django.conf import settings
from django.urls import reverse_lazy

# Create your models here.

class Room(models.Model):
    ROOM_CATEGORIES=(
        ('AC', 'Air-Conditioned'),
        ('NAC', 'Non Air-Conditioned'),
        ('DEL', 'Deluxe'),
        ('KIN', 'King'),
        ('QUE', 'Queen'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()
    room_charge = models.IntegerField()

    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} person(s) for {self.room_charge} Shillings'

class Meal(models.Model):
    MEAL_CATEGORIES=(
        ('BRE', 'Breakfast'),
        ('LUN', 'Lunch'),
        ('SUP', 'Supper'), 
    )
    meal_type = models.CharField(max_length=3, choices=MEAL_CATEGORIES)
    meal_name = models.CharField(max_length=20) 
    price = models.IntegerField() 

    def __str__(self):
        return f'{self.meal_name}. {self.meal_type} for {self.price} shillings'

class Service(models.Model): 
    SERVICE_CATEGORIES=(
        ('HSKP', 'House Keeping'),
        ('LAUN', 'Laundry'), 
    )
    service_type = models.CharField(max_length=4, choices=SERVICE_CATEGORIES)
    service_name = models.CharField(max_length=20)
    service_charge = models.IntegerField() 

    def __str__(self):
        return f'{self.service_name} for {self.service_charge} shillings'

########################################################################################

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked room {self.room}; From {self.check_in} To {self.check_out}.' 

    def get_room_category(self):
        room_categories = dict(self.room.ROOM_CATEGORIES)
        room_category = room_categories.get(self.room.category)
        return room_category
    
    def get_cancel_booking_url(self):
        return reverse_lazy('hotel:CancelBookingView', args={self.pk, })

class MealSelection(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    date = models.DateTimeField() 

    def __str__(self):
        return f'{self.user} has selected {self.meal}; On {self.date}.'  
    
    def get_meal_category(self):
        meal_categories = dict(self.meal.MEAL_CATEGORIES)
        meal_category = meal_categories.get(self.meal.meal_type)
        return meal_category

class ServiceSelection(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    service_date = models.DateField() 

    def __str__(self):
        return f'{self.user} has selected {self.service}; On {self.service_date}.'  

    def get_service_category(self):
        service_categories = dict(self.service.SERVICE_CATEGORIES)
        service_category = service_categories.get(self.service.service_type)
        return service_category