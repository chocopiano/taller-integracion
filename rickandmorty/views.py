from django.shortcuts import render
from rickandmorty.consultas_api import capitulos, informacion_e,obtener_personajes,obtener_personaje,obtener_episodios,\
    obtener_idl,obtner_lugar, obtener_residentes,personajes, lugares

def ver_capitulos(request):
    lista=capitulos()
    return render(request,'episodios.html',{'episodios':lista})

def inf_episodio(request,id):
    contenido=informacion_e(id)
    personajes=obtener_personajes(contenido)
    return render(request,'infcapitulo.html',{'contenido':contenido,'personajes':personajes})

def informacionp(request,id):
    personaje=obtener_personaje(id)
    capitulos=obtener_episodios(personaje)
    location=obtener_idl(personaje)
    return render(request,'infpersonaje.html',{'personaje':personaje,'capitulos':capitulos,'location':location})

def lugar(request,id):
    lugar=obtner_lugar(id)
    residentes=obtener_residentes(lugar)
    return render(request,'influgar.html',{'lugar':lugar,'residentes':residentes})

def buscar(request):
    if request.GET['prd']:
        palabra=request.GET['prd']
        palabra1=palabra.lower()
        lista=capitulos()
        lista1=personajes()
        lista2=lugares()
        listaa=[]
        listab=[]
        listac=[]
        for i in lista:
            j=i['nombre'].lower()
            if palabra1 in j:
                listaa.append(i)
        for i in lista1:
            j=i['nombre'].lower()
            if palabra1 in j:
                listab.append(i)
        for i in lista2:
            j=i['nombre'].lower()
            if palabra1 in j:
                listac.append(i)
        if (len(listaa)+len(listab)+len(listac)==0):
            mensaje = {'aux': False}
        else:
            mensaje={'capitulos':listaa,'personajes':listab,'lugares':listac,'aux':True}
    else:
        mensaje={'aux':False}
    return render(request,'busqueda.html',mensaje)