from django.contrib import admin
from .models import ContactForm
# Register your models here.
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('subject','email','company_name','phone','full_name')
    search_fields = ('subject','email','company_name','phone','full_name')

admin.site.register(ContactForm, ContactFormAdmin)