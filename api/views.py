from django.db.models import Q
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from api.models import Equipo, Jugador
from api.serializers import EquipoSerializer, JugadorSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'equipos': reverse('api:equipos', request=request, format=format),
        'jugadores': reverse('api:players', request=request, format=format)
    })


class EquipoListCreateAPIView(generics.ListCreateAPIView):
    # Obtiene la lista de todos los Equipos y permite crear uno nuevo
    serializer_class = EquipoSerializer
    queryset = Equipo.objects.all()


class EquipoAPIView(APIView):
    """
    Lista todos los Equipos, o crea uno nuevo.
    """

    def get(self, request, format=None):
        queryset = Equipo.objects.all()
        team = self.request.query_params.get('team')
        player = self.request.query_params.get('player')

        if team:
            queryset = queryset.filter(
                Q(id__icontains=team) | Q(name__icontains=team) | Q(city__icontains=team)
            )
        serializer = EquipoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EquipoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EquipoDetailAPIView(APIView):
    """
    Obtiene, actualiza o elimina una instancia de Equipo.
    """

    def get_object(self, pk):
        try:
            return Equipo.objects.get(pk=pk)
        except Equipo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        equipo = self.get_object(pk)
        serializer = EquipoSerializer(equipo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        equipo = self.get_object(pk)
        serializer = EquipoSerializer(equipo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        equipo = self.get_object(pk)
        equipo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JugadorListCreateAPIView(generics.ListCreateAPIView):
    # Obtiene la lista de todos los Equipos y permite crear uno nuevo
    serializer_class = JugadorSerializer
    queryset = Jugador.objects.all()


class JugadorAPIView(APIView):
    """
    Lista todos los Jugadores, o crea uno nuevo.
    """

    def get(self, request, format=None):
        queryset = Jugador.objects.all()
        player = self.request.query_params.get('player')

        if player:
            queryset = queryset.filter(
                Q(id__icontains=player) | Q(name__icontains=player) | Q(goals__icontains=player)
            )
        serializer = JugadorSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JugadorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JugadorDetailAPIView(APIView):
    """
    Obtiene, actualiza o elimina una instancia de Jugador.
    """

    def get_object(self, pk):
        try:
            return Jugador.objects.get(pk=pk)
        except Jugador.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jugador = self.get_object(pk)
        serializer = JugadorSerializer(jugador)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jugador = self.get_object(pk)
        serializer = JugadorSerializer(jugador, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jugador = self.get_object(pk)
        jugador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)