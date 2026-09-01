from django.db import models

# Create your models here.
class Consultation(models.Model):
    consultation_id = models.AutoField(primary_key=True)
    appointment = models.TextField()
    symptoms = models.TextField()
    diagnosis = models.TextField()
    consultation_date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.appointment


# {
#     "consultation_id": 101,
#     "test_id": 5,
#     "test_name": "Blood Test",
#     "status": "pending"
# }
class PrescribedLab(models.Model):

    lab_prescription_id = models.AutoField(primary_key=True)

    consultation_id = models.IntegerField()

    test_id = models.IntegerField()

    test_name = models.CharField(max_length=200)

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        COMPLETED = "completed", "Completed"

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    def __str__(self):
        return f"{self.test_name} - {self.status}"

class Doctor(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    DEPARTMENT_CHOICES = [
        ("Cardiology", "Cardiology"),
        ("Neurology", "Neurology"),
        ("Orthopedics", "Orthopedics"),
        ("Pediatrics", "Pediatrics"),
        ("Dermatology", "Dermatology"),
        ("General Medicine", "General Medicine"),
        ("General Surgery", "General Surgery"),
        ("Gynecology", "Gynecology"),
        ("ENT", "ENT"),
        ("Ophthalmology", "Ophthalmology"),
        ("Dentistry", "Dentistry"),
        ("Other", "Other"),
    ]

    BLOOD_GROUP_CHOICES = [
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("On Leave", "On Leave"),
        ("Inactive", "Inactive"),
    ]

    # Doctor ID
    doctor_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )
    name = models.CharField(max_length=100)

    # Professional Information
    department = models.CharField(
        max_length=50,
        choices=DEPARTMENT_CHOICES
    )

    fees = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    experience = models.PositiveIntegerField(
        help_text="Experience in years"
    )

    # Login Information
    username = models.CharField(
        max_length=100,
        unique=True
    )

    password = models.CharField(
        max_length=255
    )

    # Personal Information
    date_of_birth = models.DateField()

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    # Contact Information
    phone = models.CharField(
        max_length=15
    )

    email = models.EmailField(
        unique=True
    )

    blood_group = models.CharField(
        max_length=3,
        choices=BLOOD_GROUP_CHOICES,
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    emergency_contact = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active"
    )

    def save(self, *args, **kwargs):

        if not self.doctor_id:
            last_doctor = Doctor.objects.order_by("-id").first()

            if last_doctor:
                next_id = last_doctor.id + 1
            else:
                next_id = 1

            self.doctor_id = f"DOC{next_id:03d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.doctor_id} - {self.username}"