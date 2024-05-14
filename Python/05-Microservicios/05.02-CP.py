#####################################################################
# Código postal ejemplo                                             #
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
        for subdata in data["places"]:
            print(f"País: {data["country"]}")
            print(f"Ubicación: {subdata["place name"]}")
            print(f"Latitud: {subdata["latitude"]}")
            print(f"Longitud: {subdata["longitude"]}")
            print(f"Provincia: {subdata["state"]}")
            print(f"Abreviación provincia: {subdata["state abbreviation"]}")
            print(f"Latitud: {subdata["latitude"]}")
            print()
    else:
        print(f"ERROR ({response.status_code}: {response.reason}\n")   

except Exception as err:
    print(f"{err}")
    









