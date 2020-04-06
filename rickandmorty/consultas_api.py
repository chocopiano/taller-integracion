import requests

def capitulos():
    lista = []
    for m in range(1,3):
        url='https://integracion-rick-morty-api.herokuapp.com/api/episode/?page='+str(m)
        consulta=requests.get(url)
        capitulo=consulta.json()
        for i in capitulo['results']:
            lista.append({'id':i['id'],'nombre':i['name'],'fecha':i['air_date'],'codigo':i['episode']})
    return lista

def informacion_e(id):
    url = 'https://integracion-rick-morty-api.herokuapp.com/api/episode/'+id
    consulta=requests.get(url)
    episodio=consulta.json()
    return episodio

def obtener_personajes(url):
    personajes=[]
    for personaje in url['characters']:
        sujet=requests.get(personaje)
        sujeto=sujet.json()
        personajes.append({'id':sujeto['id'],'nombre':sujeto['name']})
    return personajes

def obtener_personaje(id):
    url='https://integracion-rick-morty-api.herokuapp.com/api/character/'+id
    consulta=requests.get(url).json()
    return consulta

def obtener_episodios(personaje):
    lista=personaje['episode']
    lista1=[]
    for i in lista:
        nombre=requests.get(i).json()
        lista1.append(nombre)
    return lista1



def obtener_idl(aux):
    url=aux['location']['url']
    consulta=requests.get(url).json()
    return consulta['id']

def obtner_lugar(id):
    url='https://integracion-rick-morty-api.herokuapp.com/api/location/'+id
    consulta=requests.get(url).json()
    return consulta

def obtener_residentes(aux):
    lista=[]
    for residente in aux['residents']:
        consulta=requests.get(residente).json()
        lista.append(consulta['name'])
    return lista

def personajes():
    lista=[]
    for m in range(1,26):
        url='https://integracion-rick-morty-api.herokuapp.com/api/character/?page='+str(m)
        consulta=requests.get(url).json()
        for i in consulta["results"]:
            lista.append({'id':i['id'],'nombre':i['name']})
    return lista

def lugares():
    lista=[]
    for m in range(1,5):
        url='https://integracion-rick-morty-api.herokuapp.com/api/location/?page='+str(m)
        consulta=requests.get(url).json()
        for i in consulta['results']:
            lista.append({'id':i['id'],'nombre':i['name']})
    return lista
