import json

def cargar_datos(archivo):
    datos = {}
    with open(archivo,"r") as file:
        datos=json.load(file)
    return datos

def guardar_datos(datos, archivo):
    datos = dict(datos)
    
    diccionario=json.dumps(datos, indent=4)
    file=open(archivo,"w")
    file.write(diccionario)
    file.close()
    
RUTA_BASE_DE_DATOS_ARTISTAS ="JSONfiles/artistas.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS_ARTISTAS)


