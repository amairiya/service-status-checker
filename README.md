# service-status-checker
custum service-status-checker

un exemple de réponse JSON qui pourrait être retournée par une API qui effectue un monitoring de l'état de trois API internes. Ce retour inclut le status HTTP de chaque API, ainsi que des informations supplémentaires comme le temps de réponse et la réussite ou l'échec du contrôle de santé.

'''
{
  "status": "success",
  "timestamp": "2025-02-09T15:45:00Z",
  "apis": [
    {
      "name": "API_1",
      "url": "http://internal-api1.local/health",
      "status_code": 200,
      "status": "up",
      "response_time_ms": 120,
      "message": "API is healthy"
    },
    {
      "name": "API_2",
      "url": "http://internal-api2.local/health",
      "status_code": 503,
      "status": "down",
      "response_time_ms": 350,
      "message": "API is down. Service unavailable."
    },
    {
      "name": "API_3",
      "url": "http://internal-api3.local/health",
      "status_code": 200,
      "status": "up",
      "response_time_ms": 95,
      "message": "API is healthy"
    }
  ]
}
'''
