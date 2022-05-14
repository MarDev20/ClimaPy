import time #cosa de ver si pidió a API hace 10 mins
import requests
import datetime
 
city = input("Que ciudad? 'SALIR' para salir")
apiKey = "e59e9225876fb550ac9ffb93f03b4373"


#--------------------- INPUT VALID CITY OR EXIT ------------------------------------
if city != "SALIR":
    climaReciente= requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}").json()
    latestRequest = datetime.datetime.today().minute



    #------LATEST API CALL LESS THAN 10' AGO? READ CACHE, ELSE, ASK API FOR WAETHER------------------------------------
    def clima():
        if datetime.datetime.today().minute - latestRequest < 10:
            print("Cache!")
            return climaReciente

        else:
            print("Requesteando")
            cliamReciente= requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}").json()
            return climaReciente



#------CALL THE WEATHER FUNCTION INTO ClimaObtenido------------------------

climaObtenido = clima() 


#------DIVIDE THE JSON FROM WEATHER API INTO SECTIONS: ------------------------------------

    nuevoDix={} # declare out of desglozarClima() or the recursivity in line43 resets it each loop

    def desglozarClima(diccioActual):

        for k,v in diccioActual.items(): # according to value datatype, either add to nuevoDix or recurse function
            
            if type(v) == int or type(v) == float or type(v) == str:
                nuevoDix.update({k:v})

            elif type(v) == dict:
                desglozarClima(v) #-----Recursivity here!

            elif type(v) == list:
                for i in v:
                    if type(i) == dict:
                        desglozarClima(i)
            else:
                nuevoDix.update({k:v})

        return nuevoDix #----------------Why do I have to return nuevoDix if it is a global variable?



    #----PRINT THE RESULTS
    print(f"Clima es \n {climaObtenido}")
    print("----------------------------------------------------------------")
    print( f"Desglozadito Seria \n {desglozarClima(climaObtenido)}" )






else:
  print("Saliendo")

 #request image acording to weather there
 #build an html laying that our
 #show graph with forecast
