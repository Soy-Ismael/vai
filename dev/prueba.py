def goove():
    import requests

    # URL de la API de Govee para obtener el estado de los dispositivos
    url = "https://developer-api.govee.com/v1/devices/state"

    # Tu clave de API (reemplázala con la tuya)
    api_key = '651af87f-f17f-4bc4-ad5b-ae137d5ed883'

    # Encabezados para la autenticación
    headers = {
        "Content-Type": "application/json",
        "Govee-API-Key": api_key
    }

    # Realiza una solicitud GET para obtener información sobre tus dispositivos
    response = requests.get(url, headers=headers)

    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()
        # Aquí puedes procesar los datos de la respuesta
        print(data)
    else:
        print(f"Error al obtener datos. Código de estado: {response.status_code}")

def condicional(index:int):
    import re
    if re.match(r'\d',str(index)):
        # return True
        print('True')
    

    if index in range(5):
        print(True)
    else:
        print(False)


condicional(5)
    