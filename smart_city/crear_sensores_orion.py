import requests
import json

# URL base del Orion Context Broker
ORION_URL = "http://localhost:1026/v2/entities"

# Cabeceras HTTP
headers = {"Content-Type": "application/json"}

# Definimos las tres entidades
entidades = [
    {
        "id": "sensor_calidad_H2O_1",
        "type": "CalidadH2O",
        "fecha_actual":{"type": "DateTime"},
        "ppm": {  "type": "Number" }
    },
    {
        "id": "sensor_co2_1",
        "type": "CO2",
        "fecha_actual":{"type": "DateTime"},
        "ppm": { "type": "Number"}
    },
    {
        "id": "sensor_temperatura1",
        "type": "SensorTemperaturaAgua",
        "fecha_actual":{"type": "DateTime"},
        "ph": { "type": "Number"},
        "temperatura": { "type": "Number"},
        "cloro": {"type": "Number"}
    }
]

# Crear las entidades una a una
for entidad in entidades:
    print(f"Creando {entidad['id']}...")
    response = requests.post(ORION_URL, headers=headers, data=json.dumps(entidad))
    if response.status_code == 201:
        print(f"✅ Entidad {entidad['id']} creada correctamente.")
    elif response.status_code == 422:
        print(f"⚠️ Entidad {entidad['id']} ya existe.")
    else:
        print(f"❌ Error creando {entidad['id']}: {response.status_code} - {response.text}")

print("\nConsulta de todas las entidades existentes:")
consulta = requests.get(ORION_URL)
print(json.dumps(consulta.json(), indent=4, ensure_ascii=False))

