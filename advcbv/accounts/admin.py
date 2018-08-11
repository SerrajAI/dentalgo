from django.contrib import admin
from accounts.models import Patient,Doctor,Appointment,Operation
# Register your models here.
# admin.site.register(School)
# admin.site.register(Student)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Operation)
