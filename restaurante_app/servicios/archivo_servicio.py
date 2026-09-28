# servicios/archivo_servicio.py
# Servicio encargado UNICAMENTE de la persistencia de productos, usuarios
# y ventas en JSON. No conoce reglas de negocio del restaurante
# (duplicados, stock, validez de una venta, etc.): solo sabe leer y
# escribir archivos, y convertir entre objetos y diccionarios.
import json
from pathlib import Path


class ArchivoServicio:
    def __init__(self, carpeta_datos="datos"):
        self.carpeta_datos = Path(carpeta_datos)    

    def leer_json(self, nombre_archivo):
        """Lee y retorna los datos de un archivo JSON. Retorna lista vacía si no existe o hay error."""
        ruta = self.carpeta_datos / nombre_archivo

        if not ruta.exists():
            return []
        
        with ruta.open("r", encoding="utf-8") as archivo:
                return json.load(archivo)
        

    def escribir_json(self, nombre_archivo, datos):
        """Escribe los datos provistos dentro de un archivo JSON con formato legible."""
        ruta = self.carpeta_datos / nombre_archivo
        ruta.parent.mkdir(parents=True, exist_ok=True)

        with ruta.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
            
    