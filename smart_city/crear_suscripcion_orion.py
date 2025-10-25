import requests
import json

# Endpoint de Orion
ORION_URL = "http://localhost:1026/v2/subscriptions"

# Cabeceras HTTP
headers = {"Content-Type": "application/json"}

# Definición de la suscripción
suscripcion = {
    "description": "Suscripción para enviar cambios de sensores a QuantumLeap",
    "subject": {
        "entities": [
            {
                "idPattern": ".*"  # Escucha todas las entidades
            }
        ],
        "condition": {
            "attrs": []  # Se puede dejar vacío para escuchar todos los cambios
        }
    },
    "notification": {
        "http": {
            "url": "http://quantumleap:8668/v2/notify"
        },
        "attrs": [],
        "metadata": ["dateCreated", "dateModified"]
    },
    "throttling": 5
}

# Crear la suscripción
print("Creando suscripción en Orion...")
response = requests.post(ORION_URL, headers=headers, data=json.dumps(suscripcion))

if response.status_code == 201:
    print("✅ Suscripción creada correctamente.")
elif response.status_code == 422:
    print("⚠️ La suscripción ya existe.")
else:
    print(f"❌ Error al crear la suscripción: {response.status_code} - {response.text}")

# Verificar las suscripciones existentes
print("\n🔎 Suscripciones actuales en Orion:")
consulta = requests.get(ORION_URL)
print(json.dumps(consulta.json(), indent=4, ensure_ascii=False))
