
from django.contrib import admin
from .models import FileUpload, patient, test
# Register your models here.

admin.site.register(FileUpload)
admin.site.register(patient)
admin.site.register(test)
