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
        "unidad": {"value": "ppm", "type": "Text"}
    },
    {
        "id": "sensor_co2_1",
        "type": "CO2",
        "unidad": {"value": "ppm", "type": "Text"}
    },
    {
        "id": "sensor_temperatura1",
        "type": "SensorTemperaturaAgua",
        "ph": {"value": 7.2, "type": "Float"},
        "temperatura": {"value": 26.0, "type": "Float"},
        "cloro": {"value": 1.5, "type": "Float"}
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

