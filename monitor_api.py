from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

# Liste des API internes à surveiller
api_endpoints = [
    {"name": "API_1", "url": "http://internal-api1.local/health"},
    {"name": "API_2", "url": "http://internal-api2.local/health"},
    {"name": "API_3", "url": "http://internal-api3.local/health"}
]

def check_api_status(url):
    """Fonction pour tester le statut HTTP d'une API"""
    try:
        # Effectuer un appel GET à l'API
        start_time = time.time()
        response = requests.get(url, timeout=5)  # Timeout de 5 secondes
        response_time_ms = (time.time() - start_time) * 1000  # Durée en ms

        # Vérifier le code de statut HTTP et définir l'état
        if response.status_code == 200:
            return {
                "status_code": response.status_code,
                "status": "up",
                "response_time_ms": round(response_time_ms, 2),
                "message": "API is healthy"
            }
        else:
            return {
                "status_code": response.status_code,
                "status": "down",
                "response_time_ms": round(response_time_ms, 2),
                "message": f"API is down. Received status code {response.status_code}"
            }
    except requests.exceptions.RequestException as e:
        # Si une exception se produit (par exemple, connexion impossible), retourner un statut d'erreur
        return {
            "status_code": 503,
            "status": "down",
            "response_time_ms": 0,
            "message": f"API is unreachable. Error: {str(e)}"
        }

@app.route('/api/status', methods=['GET'])
def get_api_status():
    """Route qui retourne le statut de santé de toutes les APIs internes"""
    api_status = []

    # Vérifier le statut de chaque API dans la liste
    for api in api_endpoints:
        status = check_api_status(api["url"])
        api_status.append({
            "name": api["name"],
            "url": api["url"],
            "status_code": status["status_code"],
            "status": status["status"],
            "response_time_ms": status["response_time_ms"],
            "message": status["message"]
        })
    
    # Retourner la réponse JSON avec le statut de toutes les APIs
    return jsonify({
        "status": "success",
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        "apis": api_status
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
