from django.contrib import admin
from .models import *
from AppoinmentApp.models import Appointment

# Register your models here.
admin.site.register(User)
#class AppointmentStacked(admin.StackedInline):



class AppointmentStacked(admin.TabularInline):
    model = Appointment
    extra = 1

class DoctorPersoClass(admin.ModelAdmin):
    inlines = [AppointmentStacked ,]

admin.site.register(Doctor,DoctorPersoClass)
admin.site.register(Patient)
admin.site.register(Speciality)
