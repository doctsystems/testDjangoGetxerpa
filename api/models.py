from django.db import models


class Equipo(models.Model):
    # modelo para la entidad Equipo
    name = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("id", )
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

    def __str__(self):
        return self.name


class Jugador(models.Model):
    # modelo para la entidad Jugador
    name = models.CharField(max_length=255)
    goals = models.IntegerField(default=0)
    team = models.ForeignKey(Equipo, related_name="players", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name", )
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"

    def __str__(self):
        return f'{self.name}, {self.goals} goals'
