from django.contrib import admin
from .models import Appointment
from AccountApp.models import Doctor

# Register your models here.
#admin.site.register(Appointment)

#class DoctorPerso(admin.StackedInline):
#    model = Doctor

@admin.action(description='Confirmer les rendez-vous sélectionnés')
def confirmed_appointment(model, req, queryset):
    queryset.update(status='CONFIRMED')

@admin.register(Appointment)
class AppointmentAdminPers(admin.ModelAdmin):
    #inlines = [DoctorPerso]
    actions = [confirmed_appointment]
    list_display = ('reason', 'duration_minutes', 'appointment_date', 'status', 'patient')
    list_filter = ('status', 'appointment_date')
    list_editable = ('status',)
    search_fields = ('status', 'reason')
    list_per_page = 2
    ordering = ('-appointment_date',)
    fieldsets = (
        ('Description', {
            'fields': ('reason', 'status')
        }),
        ('Date + duration', {
            'fields': ('appointment_date', 'duration_minutes', 'prescription')
        }),
        ('Patient / Doctor', {
            'fields': ('patient', 'doctor')
        }),
        ('Planification', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')