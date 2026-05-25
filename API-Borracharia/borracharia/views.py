from django.shortcuts import render
from borracharia.models import user, ticket, lista
from borracharia.serializers import userSerializer, ticketSerializer, listaSerializer, listaUserSerializer, listaTicketSerializer
from rest_framework import viewsets, generics


class userViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer
class ticketViewSet(viewsets.ModelViewSet):
    queryset = ticket.objects.all()
    serializer_class = ticketSerializer

class listaViewSet(viewsets.ModelViewSet):
    queryset = lista.objects.all()
    serializer_class = listaSerializer

class listaUser(generics.ListAPIView):
    def get_queryset(self):
        queryset = lista.objects.filter(user_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = listaUserSerializer

class listaTicket(generics.ListAPIView):
    def get_queryset(self):
        queryset = lista.objects.filter(ticket_id=self.kwargs['pk'])
        return queryset
    serializer_class = listaTicketSerializer