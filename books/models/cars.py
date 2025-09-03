from django.db import models

class Cars(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    manufacturer_date = models.DateTimeField()

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.color})"
