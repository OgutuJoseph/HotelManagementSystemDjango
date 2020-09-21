from django.contrib import admin
from .models import Room, Meal, Service, Booking, MealSelection, ServiceSelection

# Register your models here.
admin.site.register(Room)
admin.site.register(Meal)
admin.site.register(Service)
admin.site.register(Booking)
admin.site.register(MealSelection)
admin.site.register(ServiceSelection)