import requests

# URL de l'API de monitoring
api_url = "http://monitoring-api.local/status"

# Effectuer l'appel GET à l'API de monitoring
response = requests.get(api_url)

# Vérifier si la réponse est valide
if response.status_code == 200:
    # Afficher le retour JSON
    monitoring_status = response.json()
    print(monitoring_status)
else:
    print(f"Erreur de connexion à l'API de monitoring: {response.status_code}")
