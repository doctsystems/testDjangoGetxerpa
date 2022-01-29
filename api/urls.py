from django.urls import path
from api.views import api_root
from api.views import EquipoListCreateAPIView, JugadorListCreateAPIView
from api.views import EquipoAPIView, EquipoDetailAPIView, JugadorAPIView, JugadorDetailAPIView

app_name = 'api'

urlpatterns = [
    path('', api_root),
    path('teams/', EquipoListCreateAPIView.as_view(), name='teams'),
    path('players/', JugadorListCreateAPIView.as_view(), name='players'),
    path('equipos/', EquipoAPIView.as_view(), name='equipos'),
    path('equipos/<int:pk>/', EquipoDetailAPIView.as_view(), name='equipo-detail'),
    path('jugadores/', JugadorAPIView.as_view(), name='jugadores'),
    path('jugadores/<int:pk>/', JugadorDetailAPIView.as_view(), name='jugador-detail'),
]