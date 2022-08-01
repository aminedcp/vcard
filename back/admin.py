from django.contrib import admin
from .models import *
from fieldsets_with_inlines import FieldsetsInlineMixin
from admin_searchable_dropdown.filters import AutocompleteFilter
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)

 

class PaysAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom']
admin.site.register(Pays,PaysAdmin)

class OrganismeAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom']
admin.site.register(Organisme,OrganismeAdmin)

class OrganismeFilter(AutocompleteFilter):
    title = 'Organisme' # display title
    field_name = 'organisme' # name of the foreign key field    
    
class InformationvcardAdmin(FieldsetsInlineMixin,admin.ModelAdmin):
    list_display = ('nom','prenom','telephoneperso1', 'organisme')
    search_fields = ('nom','prenom','nomar','prenomar')
    list_filter = (
        OrganismeFilter,
    )
    autocomplete_fields = ['pays','organisme']
    fieldsets_with_inlines = [
     ('CARTE DE VISITE', {
                'fields': ['cv_recto', 'cv_verso'], 'classes': ['arriveeclass']
        }),
        ('INFORMATIONS PERSONNELS', {
                'fields': ['nom', 'prenom', 'nomar', 'prenomar','pays','profession','telephoneperso1','telephoneperso2','emailperso','note'], 'classes': ['arriveeclass']
        }),
         ('INFORMATIONS ORGANISME', {
                'fields': ['organisme', 'Adressepro', 'telephonepro1','telephonepro2','emailorganisme1','emailorganisme2','fax','site_web'], 'classes': ['arriveeclass']
        }),       

        
    ]
admin.site.register(Informationvcard,InformationvcardAdmin)