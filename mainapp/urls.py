from django.urls import path, include
from .views import *

urlpatterns = [
    
    path('', Home, name="Home"),
    path('about/', About, name= "About"),
    path('temporadas/', Temporadas, name = "Temporadas"),
    path('personajes/', Personajes, name="Personajes"),
    path('update_personaje/<id_personaje>/', Formulario_Update_Personajes, name="update_personaje"),
    path('delete_personaje/<id_personaje>/', Delete_Personaje, name="delete_personaje"),
    path('formulario_personaje/', Formulario_Create_Personaje, name="formulario_personaje"),
    path('formulario_suscripcion/', Formulario_Suscripcion, name="formulario_suscripcion"),
    path('update_temporada/<id_temporada>/',Formulario_Update_Temporada, name="update_temporada"),
    path('formulario_temporada/', Formulario_Create_Temporada, name="formulario_temporada"),
    path('delete_temporada/<id_temporada>/', Delete_Temporada, name="delete_temporada"),
    path('update_suscriptor/<id_suscriptor>/', Formulario_Update_Suscriptor, name="update_suscriptor"),
    path('suscriptores/', Mostrar_Suscriptores, name="suscriptores"),
    path('delete_suscriptor/<id_suscriptor>/', Delete_Suscriptor, name="delete_suscriptor"),
    path('buscar_personaje/', Buscar_Personaje, name="buscar_personaje")
]
