from django.db import models

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField()
    number = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def state(self):
        last_move = CarMove.objects.filter(car=self).last()
        if last_move:
            if last_move.start_date and not last_move.end_date:
                return "busy"
            return "available"


class CarMove(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField()
    
    def __str__(self):
        return self.car.name
