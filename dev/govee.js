// URL de la API de Govee
const url = "https://developer-api.govee.com/v1/devices";

// Tu clave de API (reemplázala con la tuya)
const apiKey = "651af87f-f17f-4bc4-ad5b-ae137d5ed883";

// Encabezados para la autenticación
const headers = {
    "Content-Type" : "application/json",
    "Govee-API-Key" : '651af87f-f17f-4bc4-ad5b-ae137d5ed883'
};

// Realiza una solicitud GET para obtener información sobre tus dispositivos
axios
    .get(url, {headers})
    .then((response) => {
        const data = response.data;
        // Aquí puedes procesar los datos de la respuesta
        console.log(data);
        console.log(data.data);
    })
    .catch((error) => {
        console.error(`Error al obtener datos: ${error.message}`);
    });
