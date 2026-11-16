from django.db import models
from AccountApp.models import Doctor , Patient

# Create your models here.

class Appointment(models.Model):

    reason = models.TextField()
    prescription = models.FileField(
        upload_to='prescriptions/', 
        blank=True,
        null=True
    )
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'En Attente'
        COMPLETED = 'CONFIRMED', 'Confirmé'
        CANCELED = 'CANCELED', 'Annulé'

    status = models.CharField(max_length=20, choices=Status.choices , default=Status.PENDING)
    #status = models.CharField(max_length=20, choices=[  ( Status.PENDING),(Status.COMPLETED),(Status.CANCELED)])

    duration_minutes = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    appointment_date = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    #patient = models.ForeignKey("AccountApp.Patient", on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')

    class Meta: #comparer
        ordering = ['-appointment_date']
        constraints = [
            models.UniqueConstraint(
                fields=['doctor', 'appointment_date'],
                name='unicite_patient_doctor_date',
                violation_error_message='This doctor already has an appointment at this date and time.'
            )
        ]


