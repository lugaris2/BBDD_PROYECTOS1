import requests
import json
from datetime import datetime, timedelta
import random

i=0
while i<400:

    #inicio del for in
    fecha_inicio= datetime(2025, 5, 1)
    fecha_actual = fecha_inicio

    #************************************************************************************************
    # URL del Orion Context Broker sensor_temperatura1
    ORION_URL = "http://localhost:1026/v2/entities/sensor_temperatura1/attrs"

    # Encabezados
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Datos a actualizar

    data = {
        "ph": {"value": 8.2,"type": "Float"},
        "fecha_actual":{"value": fecha_actual,"type": datetime},
        "temperatura": { "value": 26.0, "type": "Float" },
        "cloro": { "value": 1.5, "type": "Float" }
        }
        

    # Enviamos la petición PATCH
    response = requests.patch(ORION_URL, headers=headers, data=json.dumps(data))

    # Mostramos el resultado
    if response.status_code == 204:
        print("✅ Actualización correcta en Orion")
    else:
        print("❌ Error al actualizar:", response.status_code, response.text)

    #***************************************************************************************




fecha_actual += timedelta(days=1)

i+=1
#nueva linea