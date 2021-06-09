from django.db import models

# Create your models here.
class ContactForm(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=500)
    phone = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    message= models.CharField(max_length=500)