from django.db import models
from django.contrib.auth.models import User

class PGListing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    available_from = models.DateField()

    def __str__(self):
        return f"{self.title} - {self.location}"
