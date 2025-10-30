import requests
import json

# Endpoint de Orion
ORION_URL = "http://localhost:1026/v2/subscriptions"

# Cabeceras HTTP
headers = {"Content-Type": "application/json"}

# Definición de las suscripciones
suscripciones = [
    {
        "description": "Suscripción para sensor_temperatura1",
        "subject": {
            "entities": [
                {
                    "id": "sensor_temperatura1",
                    "type": "SensorTemperaturaAgua"
                }
            ],
            "condition": {
                "attrs": ["fecha_actual", "ph", "temperatura", "cloro"]
            }
        },
        "notification": {
            "http": {
                "url": "http://quantumleap:8668/v2/notify"
            },
            "attrs": ["fecha_actual", "ph", "temperatura", "cloro"],
            "metadata": ["dateCreated", "dateModified"]
        },
        "throttling": 1
    },
    {
        "description": "Suscripción para sensor_calidad_H2O_1",
        "subject": {
            "entities": [
                {
                    "id": "sensor_calidad_H2O_1",
                    "type": "CalidadH2O"
                }
            ],
            "condition": {
                "attrs": ["fecha_actual", "ppm"]
            }
        },
        "notification": {
            "http": {
                "url": "http://quantumleap:8668/v2/notify"
            },
            "attrs": ["fecha_actual", "ppm"],
            "metadata": ["dateCreated", "dateModified"]
        },
        "throttling": 1
    },
    {
        "description": "Suscripción para sensor_co2_1",
        "subject": {
            "entities": [
                {
                    "id": "sensor_co2_1",
                    "type": "CO2"
                }
            ],
            "condition": {
                "attrs": ["fecha_actual", "ppm"]
            }
        },
        "notification": {
            "http": {
                "url": "http://quantumleap:8668/v2/notify"
            },
            "attrs": ["fecha_actual", "ppm"],
            "metadata": ["dateCreated", "dateModified"]
        },
        "throttling": 1
    }
]

# Crear las suscripciones
for suscripcion in suscripciones:
    print(f"Creando suscripción en Orion para {suscripcion['description']}...")
    response = requests.post(ORION_URL, headers=headers, data=json.dumps(suscripcion))

    if response.status_code == 201:
        print(" Suscripción creada correctamente.")
    elif response.status_code == 422:
        print(" La suscripción ya existe.")
    else:
        print(f" Error al crear la suscripción: {response.status_code} - {response.text}")

# Verificar las suscripciones existentes
print("\n Suscripciones actuales en Orion:")
consulta = requests.get(ORION_URL)
print(json.dumps(consulta.json(), indent=4, ensure_ascii=False))