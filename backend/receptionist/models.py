from django.db import models


class Patient(models.Model):

    patient_id = models.AutoField(primary_key=True)

    full_name = models.CharField(max_length=150)

    date_of_birth = models.DateField()

    gender = models.CharField(
        max_length=10,
        choices=[
            ("Male", "Male"),
            ("Female", "Female"),
            ("Other", "Other"),
        ]
    )

    phone = models.CharField(max_length=15)

    email = models.EmailField(
        blank=True,
        null=True
    )

    blood_group = models.CharField(
        max_length=5,
        blank=True,
        null=True
    )

    address = models.TextField()

    emergency_contact = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    allergies = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=[
            ("Active", "Active"),
            ("Admitted", "Admitted"),
            ("Discharged", "Discharged"),
        ],
        default="Active"
    )

    registered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name