from django.contrib import admin
from .models import Persona, TeamMember, MainBranches

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display= ['id', 'name', 'message', 'createdat']
admin.site.register(Persona, PersonaAdmin)

class TeamMemberAdmin(admin.ModelAdmin):
    list_display= ['id', 'name', 'designation', 'createdat']
admin.site.register(TeamMember, TeamMemberAdmin)

class MainBranchesAdmin(admin.ModelAdmin):
    list_display= ['id', 'image', 'postalcode', 'createdat']

admin.site.register(MainBranches, MainBranchesAdmin)
