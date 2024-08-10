from django.shortcuts import render
from .models import TeamMember, Persona

def about(request):
    team_members = TeamMember.objects.all()[:4]
    personas = Persona.objects.all()[:6]
    return render(request, 'about/about.html', {'team_members':team_members, 'personas': personas})

def team(request):
    team_members = TeamMember.objects.all()
    return render(request, 'about/members.html', {'team_members':team_members})

def persona(request):
    personas = Persona.objects.all()
    return render(request, 'about/personas.html', {'personas':personas})

def privacy(request):
    return render(request, 'about/privacy-policy.html')

def purchaseGuide(request):
    return render(request, 'about/purchase-guide.html')

def terms(request):
    return render(request, 'about/terms.html')