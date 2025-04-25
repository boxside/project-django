from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Parameter(models.Model):
    id_param = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15, decimal_places=6)
    updated_at = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.title