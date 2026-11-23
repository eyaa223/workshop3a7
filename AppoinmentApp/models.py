from django.db import models
from AccountApp.models import Doctor , Patient
from django .utils import timezone 
from django.core.exceptions import ValidationError

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

    def clean(self):
        modified_date = self._state.adding or (
            Appointment.objects.filter(
                pk=self.pk, appointment_date=self.appointment_date
            ).exists()
        )
        if modified_date and self.appointment_date < timezone.now():
            raise ValidationError('la date doit être postérieure à la date d\'aujourd\'hui.')

    class Meta: #comparer
        ordering = ['-appointment_date']
        constraints = [
            models.UniqueConstraint(
                fields=['doctor', 'appointment_date'],
                name='unicite_patient_doctor_date',
                violation_error_message='Ce médecin a déjà un rendez-vous à cette date et heure.'
            )
        ]
    def __str__(self):
        return f"le rdv est pour la raison {self.reason}"

    


