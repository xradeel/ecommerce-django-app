from django import forms
from .models import ContactUs

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name','email','contact','subject','message', 'accesstoken']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Your Email'}),
            'contact': forms.TextInput(attrs={'placeholder': 'Your Phone'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message'}),
        }