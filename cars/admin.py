from django.contrib import admin
from .models import Car, CarMove
# Register your models here.


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "color", "year", "description", "number", "state")
    search_fields = ("name", "color", "year", "description", "number")
    readonly_fields = ("state",)


@admin.register(CarMove)
class CarMoveAdmin(admin.ModelAdmin):
    list_display = ("car", "start_date", "end_date", "description")
    search_fields = ("car__number", "start_date", "end_date", "description")
