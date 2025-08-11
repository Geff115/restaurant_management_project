from django.db import models

# Creating the Restaurant model.

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name