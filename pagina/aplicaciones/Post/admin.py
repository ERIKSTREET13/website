from django.contrib import admin
from .models import Categoria
from .models import Autor
from .models import Miembro
from .models import Evento

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['name']

    list_display = ('id','name','status','create_date')

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['autName1']

    list_display = ('id','autName1','autName2','autSurname1','autSurname2','autMail','autStatus')

class MiembroAdmin(admin.ModelAdmin):
    search_fields = ['miemName1']

    list_display = ('id','miemName1','miemName2','miemSurname1','miemSurname2','miemOcu','miemPho1','miemPho2','miemCrea','miemDesc')

class EventoAdmin(admin.ModelAdmin):
    search_fields = ['event_date']

    list_display = ('id','event_date','event_time','primary_street','secondary_street','house_number','city','description','image','created_date','status')

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Miembro,MiembroAdmin)
admin.site.register(Evento,EventoAdmin)