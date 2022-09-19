"""
Definition of models.
"""

from django.db import models

# Create your models here.

class patient(models.Model):
    ID = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length = 200)
    nationalID = models.CharField(max_length = 14)
    phone = models.CharField(max_length = 11)

    def __str__(self):
         return str(self.ID)


class FileUpload(models.Model):
    ID = models.AutoField(primary_key=True)
    patientID = models.ForeignKey(patient, on_delete=models.CASCADE, blank=True, null=True)
    dicomImg = models.FileField(upload_to="dicom")
    modality = models.CharField(max_length = 20, blank=True, null=True)

    def __str__(self):
         return str(self.ID)

class test(models.Model):
     dicomImg = models.FileField(upload_to="dicom")


