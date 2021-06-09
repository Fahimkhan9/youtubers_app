from django.shortcuts import render, redirect
from .models import ContactForm
from django.contrib import messages
# Create your views here.

#  full_name = models.CharField(max_length=100)
#     email = models.CharField(max_length=50)
#     subject = models.CharField(max_length=500)
#     phone = models.CharField(max_length=100)
#     company_name = models.CharField(max_length=100)
#     message= models.CharField(max_length=500)
def contactform(request):
    print(request.method)
    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        company_name = request.POST['company_name']
        message = request.POST['message']
        print(
            full_name,
            email,
            subject,
            phone,
            company_name,
            message
        )
    contactform = ContactForm(full_name=full_name,email=email,subject=subject,phone=phone,company_name=company_name,message=message)
    contactform.save()
    messages.success(request, 'Thanks for contacting!')
        
    return redirect('contact')


    