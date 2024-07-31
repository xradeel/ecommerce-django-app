from django.shortcuts import render
from .models import ContactUs

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        telephone = request.POST['telephone']
        subject = request.POST['subject']
        message = request.POST['message']
        accesstoken = request.POST['csrfmiddlewaretoken']
        
        contact_us = ContactUs(name=name, email=email, contact=telephone, subject=subject, message=message, accesstoken=accesstoken)
        contact_us.save()

        
        
    return render(request, 'contact/contact.html')
