from django.db import models

class Restaurant(models.Model):
    """
    Restaurant model
    """
    name = models.CharField(max_length=255)
    location = models.Charfield(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_add_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name