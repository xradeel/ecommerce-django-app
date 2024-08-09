from django.shortcuts import render
from .models import ContactUs
from .forms import ContactForm
from uuid import uuid4

def contact(request):
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     telephone = request.POST['telephone']
    #     subject = request.POST['subject']
    #     message = request.POST['message']
    #     accesstoken = request.POST['csrfmiddlewaretoken']
        
    #     contact_us = ContactUs(name=name, email=email, contact=telephone, subject=subject, message=message, accesstoken=accesstoken)
    #     contact_us.save()
    custom_token_value = uuid4()
    if request.method == 'POST':
        filled_form = ContactForm(request.POST)
        if filled_form.is_valid():
            note = 'Thanks for contact us,'
            filled_form.save()
            new_form = ContactForm(initial={'accesstoken': custom_token_value})  
            return render(request, 'contact/contact.html', {'ContactFrom': new_form, 'note':note})
    else:
        form = ContactForm(initial={'accesstoken': custom_token_value})  
        return render(request, 'contact/contact.html', {'ContactFrom':form})
