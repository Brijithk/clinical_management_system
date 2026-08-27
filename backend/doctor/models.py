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