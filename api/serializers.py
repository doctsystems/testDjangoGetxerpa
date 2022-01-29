from rest_framework import serializers

from .models import Equipo, Jugador

from django.db.models import Sum


class JugadorSerializer(serializers.ModelSerializer):
    # serializador para el modelo Jugador

    class Meta:
        model = Jugador
        fields = ('id', 'name', 'goals', 'team', 'created_at', 'updated_at')
        read_only_fields = ('id', )


class EquipoSerializer(serializers.ModelSerializer):
    # serializador para el modelo Equipo
    players = serializers.StringRelatedField(many=True, read_only=True)
    goals_count = serializers.SerializerMethodField("get_goals_count", default=0)

    class Meta:
        model = Equipo
        fields = ('id', 'name', 'city', 'players', 'goals_count', 'created_at', 'updated_at')
        read_only_fields = ('id', )
        # extra_kwargs = {'id': {'read_only': True}, 'players': {'read_only': True}}

    def get_goals_count(self, data):
        goals_sum = Jugador.objects.filter(team=data.id).aggregate(Sum('goals'))['goals__sum']
        return goals_sum if goals_sum is not None else 0
