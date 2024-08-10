from django.urls import path
from . import views

app_name = 'about'
urlpatterns = [
    path('', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy.policy'),
    path('purchase/', views.purchaseGuide, name='about.purchase.guide'),
    path('terms/', views.terms, name='about.terms'),
    path('team/', views.team, name='about.team'),
    path('persona/', views.persona, name='about.persona'),
]
