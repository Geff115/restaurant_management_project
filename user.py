from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    The Profile model extends the built-in User model
    using a OneToOneField.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username