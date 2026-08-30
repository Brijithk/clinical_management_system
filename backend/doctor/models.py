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