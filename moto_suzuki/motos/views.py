from django.shortcuts import render, redirect
from .models import moto
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def lista_motos(request):
    motos = moto.objects.all().values()
    return JsonResponse(list(motos), safe = False)

@csrf_exempt
def crear_moto(request):
    if request.method == "POST":
        data = json.loads(request.body)
        nueva_moto = moto.objects.create(
            modelo=data.get("modelo"),
            tipo_moto=data.get("tipo_moto"),
            cilindrada=data.get("cilindrada"),
            potencia=data.get("potencia"),
            precio=data.get("precio"),
        )
        return JsonResponse({"message": "Moto creada", "id": nueva_moto.id})


def detalle_moto(request, id):
    try:
        moto_obj = moto.objects.get(id=id)
        return JsonResponse({
            "id": moto_obj.id,
            "modelo": moto_obj.modelo,
            "tipo_moto": moto_obj.tipo_moto,
            "cilindrada": moto_obj.cilindrada,
            "potencia": moto_obj.potencia,
            "precio": moto_obj.precio,
        })
    except moto.DoesNotExist:
        return JsonResponse({"error": "Moto no encontrada"}, status=404)

@csrf_exempt
def actualizar_moto(request, id):
    if request.method == "PUT":
        data = json.loads(request.body)
        try:
            moto_obj = moto.objects.get(id=id)
            moto_obj.modelo = data.get("modelo", moto_obj.modelo)
            moto_obj.tipo_moto = data.get("tipo_moto", moto_obj.tipo_moto)
            moto_obj.cilindrada = data.get("cilindrada", moto_obj.cilindrada)
            moto_obj.potencia = data.get("potencia", moto_obj.potencia)
            moto_obj.precio = data.get("precio", moto_obj.precio)
            moto_obj.save()
            return JsonResponse({"message": "Moto actualizada"})
        except moto.DoesNotExist:
            return JsonResponse({"error": "Moto no encontrada"}, status=404)
        

@csrf_exempt
def eliminar_moto(request, id):
    if request.method == "DELETE":
        try:
            moto_obj = moto.objects.get(id=id)
            moto_obj.delete()
            return JsonResponse({"message": "Moto eliminada"})
        except moto.DoesNotExist:
            return JsonResponse({"error": "Moto no encontrada"}, status=404)
