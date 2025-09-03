from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    published_date = models.DateField()

    def __str__(self):
        return self.title