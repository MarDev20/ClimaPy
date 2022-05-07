APP DE CLIMA

Se conecta a OpenWeatherMap.org
 we recommend making API calls less than once/10mins per location (by city name, geocoords or zip).OpenWeather model udpates once in 10 minutes.

Recupera clima de una city.

Instalar request
 $ python -m pip install requests

...y...

 >>> import requests
 >>> response = requests.get( "https://jsonplaceholder.typicode.com/todos/1" )
 >>> response.json()
     {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}

Qué debe mandarse a mano o implícito en una request?
 Metodo / Endpoint / Protocolo y versión / Host Url / ContentType

  PATCH /cars/4 HTTP/1.1
  Host: api.example.com
  Content-Type: application/json

OPENWEATHER es:
 https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid={API key}
 https://api.openweathermap.org/data/2.5/weather?q=Monntevideo,uy&appid={API key}

METODOS
 GET trae data
 POST créa (devolvé ID creada asi podemo laburarla)
 PUT modifica todo el item
 PATCH parte del item
 DELETE duh!


USAR ASI
 import time: #cosa de ver si pidió a API hace 10 mins
 import requests
 import datetime

 input(que ciudad)
 cliamReciente= tomar climaReciente desde openWeather

 #luego una funcion que vea si requestáa o dá lo cacehado

 def clima():
   tiempoDesdeUltimaRequestAPI = datetime.datetime.today().minute
   if datetime.datetime.today().minute - tiempoDesdeUltimaRequestAPI > 10mins:
     return climaReciente
   else 
     climaRecienre request openWeathe for that place
     return climaReciente

 request image acording to weather there
 build an html laying that our
 show graph with forecast
