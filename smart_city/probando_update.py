import matplotlib as plt
import requests
import json
from datetime import datetime, timedelta
import random
import pandas as pd
import numpy as np


def sensor_temperatura_agua():

       # URL del Orion Context Broker sensor_temperatura1 TEMPERATURA DEL AGUA *********
    ORION_URL = "http://localhost:1026/v2/entities/sensor_temperatura1/attrs"

    # Encabezados
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    i=0
    fecha_inicio= datetime(2025, 5, 1)
    data_list=[]
    while i<20:

        #inicio del for in
        
        fecha_actual = fecha_inicio
        ph= round(random.uniform(5,9),2)
        temperatura= round(random.uniform(-10,50),2)
        cloro= round(random.uniform(0,3),2)

        data = {
            "fecha_actual":{"value": fecha_actual,"type": datetime},
            "ph": {"value": ph,"type": "Float"},
            "temperatura": { "value": temperatura, "type": "Float" },
            "cloro": { "value": cloro, "type": "Float" }
            }
        
            # Enviamos la petición PATCH
        response = requests.patch(ORION_URL, headers=headers, data=json.dumps(data))

        # Mostramos el resultado
        if response.status_code == 204:
            print("✅ Actualización correcta en Orion")
        else:
            print("❌ Error al actualizar:", response.status_code, response.text)
        
        data_list.append(data)

        fecha_inicio += timedelta(days=1)
        i+=1
    df_data= pd.DataFrame(data_list)
    print(df_data)

sensor_temperatura_agua()

def sensor_calidad_H2O_1():

       # URL del Orion Context Broker sensor_temperatura1 TEMPERATURA DEL AGUA *********
    ORION_URL = "http://localhost:1026/v2/entities/sensor_calidad_H2O_1/attrs"

    # Encabezados
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    i=0
    fecha_inicio= datetime(2025, 5, 1)
    data_list=[]
    while i<20:

        #inicio del for in
        
        fecha_actual = fecha_inicio
        ppm= round(random.uniform(5,9),2)
        
        data = {
            "fecha_actual":{"value": fecha_actual,"type": datetime},
            "ppm": {"value": ppm,"type": "Float"},
            
            }
        
            # Enviamos la petición PATCH
        response = requests.patch(ORION_URL, headers=headers, data=json.dumps(data))

        # Mostramos el resultado
        if response.status_code == 204:
            print("✅ Actualización correcta en Orion")
        else:
            print("❌ Error al actualizar:", response.status_code, response.text)
        
        data_list.append(data)

        fecha_inicio += timedelta(days=1)
        i+=1
    df_data= pd.DataFrame(data_list)
    print(df_data)



def sensor_co2_1():

       # URL del Orion Context Broker sensor_temperatura1 TEMPERATURA DEL AGUA *********
    ORION_URL = "http://localhost:1026/v2/entities/sensor_co2_1/attrs"

    # Encabezados
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    i=0
    fecha_inicio= datetime(2025, 5, 1)
    data_list=[]
    while i<20:

        #inicio del for in
        
        fecha_actual = fecha_inicio
        ppm= round(random.uniform(5,9),2)
        
        data = {
            "fecha_actual":{"value": fecha_actual,"type": datetime},
            "ppm": {"value": ppm,"type": "Float"},
            
            }
        
            # Enviamos la petición PATCH
        response = requests.patch(ORION_URL, headers=headers, data=json.dumps(data))

        # Mostramos el resultado
        if response.status_code == 204:
            print("✅ Actualización correcta en Orion")
        else:
            print("❌ Error al actualizar:", response.status_code, response.text)
        
        data_list.append(data)

        fecha_inicio += timedelta(days=1)
        i+=1
    df_data= pd.DataFrame(data_list)
    print(df_data)




sensor_calidad_H2O_1()
sensor_co2_1()
sensor_temperatura_agua()