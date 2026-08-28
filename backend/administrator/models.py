from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    # Remove Django's default id and username
    id = None
    username = None

    user_id = models.AutoField(primary_key=True)

    user_name = models.CharField(
        max_length=100,
        unique=True
    )
    class Role(models.TextChoices):
        STAFF = "staff", "Staff"
        DOCTOR = "doctor", "Doctor"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STAFF
    )

    def __str__(self):
        return self.username