from rest_framework import serializers
from borracharia.models import user, ticket, lista

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id','nome','email','celular', 'tipo_usuario']

class ticketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ticket
        fields = '__all__'

class listaSerializer(serializers.ModelSerializer):
    class Meta:
        model = lista
        exclude = []

class listaUserSerializer(serializers.ModelSerializer):
    ticket = serializers.ReadOnlyField(source='ticket.descricao')
    class Meta:
        model = lista
        fields = ['ticket']

def get_periodo(self, obj):
    return obj.get_periodo_display()
class listaTicketSerializer(serializers.ModelSerializer):
    user_nome = serializers.ReadOnlyField(source='user.nome')
    class Meta:
        model = lista
        fields = ['user_nome']