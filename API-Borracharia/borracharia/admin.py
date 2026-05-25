from django.contrib import admin
from borracharia.models import user, ticket, lista

class users(admin.ModelAdmin):
    list_display = ('id','nome','email','celular', 'tipo_usuario',)
    list_display_links = ('id','nome',)
    list_per_page = 20
    search_fields = ('nome',)

admin.site.register(user,users)

class tickets(admin.ModelAdmin):
    list_display = ('id','codigo','descricao_servico')
    list_display_links = ('id','codigo',)
    search_fields = ('codigo',)

admin.site.register(ticket,tickets)

class listas(admin.ModelAdmin):
    list_display = ('id','user','ticket')
    list_display_links = ('id',)

admin.site.register(lista,listas)