# testDjangoGetxerpa
 Test de Django para Getxerpa


### Descripción
Tenemos dos entidades: Jugador y Equipo

* Jugador
    - id: int
    - name: str
    - goals: int
    - created_at: datetime
    - updated_at: datetime
* Equipo
    - id: int
    - name: str
    - city: str
    - created_at: datetime
    - updated_at: datetime


### Requerimientos
* Se deben relacionar las entidades y hacer un CRUD de cada una.
* Al consultar la información de un equipo, se deberá mostrar un valor adicional "goals_count" de sólo lectura, que traerá el número de goles anotados por todos sus jugadores.
* Habilitar la opción para consultar por query parameters en los métodos GET.
