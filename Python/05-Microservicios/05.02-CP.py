#####################################################################
# Trabajando con Request                                            #
#####################################################################

# Importar los módulos necesarios
import requests, pprint

cp = input("Indica un código postal: ")

endpoint = f"http://api.zippopotam.us/es/{cp}"

try: 
    response = requests.get(endpoint)

    print(f"Estado: {response.status_code} / {response.reason}")

    if(response.status_code == 200):
        data = response.json()
        for resultado in data["places"]:
            print(f"País: {data["country"]}")
            print(f"Ubicación: {resultado["place name"]}")
            print(f"Latitud: {resultado["latitude"]}")
            print(f"Longitud: {resultado["longitude"]}")
            print(f"Provincia: {resultado["state"]}")
            print(f"Abreviación provincia: {resultado["state abbreviation"]}")
            print(f"Latitud: {resultado["latitude"]}")
            print()
    else:
        print(f"ERROR ({response.status_code}: {response.reason}\n")   

except Exception as err:
    print(f"{err}")
    









