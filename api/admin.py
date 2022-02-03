from django.contrib import admin

from api.models import Equipo, Jugador


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "city", "created_at", "updated_at"]


@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "goals", "team"]


# admin.site.register(Equipo)
# admin.site.register(Jugador)
