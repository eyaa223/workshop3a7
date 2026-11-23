
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.validators import RegexValidator
class Speciality(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Speciality'
        verbose_name_plural = 'Specialities'

# Create your models here.
class User(AbstractUser):
    pass

class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True, validators=[MinLengthValidator(6)]) 
    phone = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    #specialities = models.ManyToManyField('AccountApp.Speciality')
    specialities = models.ManyToManyField('Speciality', related_name='doctors')

number_validator = RegexValidator(
    regex=r'^\d{8}$',
    message='National ID must be exactly 8 digits.'
)

def validate_birth_date(value):
    if value >= timezone.localdate():
        raise ValidationError('Birth date must be in the past.')
    
class Patient(User):
    national_id = models.CharField(max_length=8,unique=True, validators=[number_validator])

    phone = models.CharField(max_length=8)
    birth_date = models.DateField(validators=[validate_birth_date])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'


