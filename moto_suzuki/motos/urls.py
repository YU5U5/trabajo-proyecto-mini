from django.urls import path
from . import views

urlpatterns = [
    path('motos/', views.lista_motos, name='lista_motos'),
    path('motos/crear/', views.crear_moto, name='crear_moto'),
    path('motos/detalle/<int:id>/', views.detalle_moto, name='detalle_moto'),
    path('motos/actualizar/<int:id>/', views.actualizar_moto, name='actualizar_moto'),
    path('motos/eliminar/<int:id>/', views.eliminar_moto, name='eliminar_moto'),
]