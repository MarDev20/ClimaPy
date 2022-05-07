import time #cosa de ver si pidió a API hace 10 mins
import requests
import datetime
 
city = input("Que ciudad? 'SALIR' para salir")
apiKey = "e59e9225876fb550ac9ffb93f03b4373"


if city != "SALIR":
    climaReciente= requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}").json()
    latestRequest = datetime.datetime.today().minute

    def clima():#luego una funcion que vea si requestáa o dá lo cacheado
        if datetime.datetime.today().minute - latestRequest < 10:
            print("Cache!")
            print (climaReciente)
            return climaReciente

        else:
            print("Requesteando")
            cliamReciente= requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}").json()
            print (climaReciente)
            return climaReciente

    clima()

else:
  print("Saliendo")

 #request image acording to weather there
 #build an html laying that our
 #show graph with forecast
