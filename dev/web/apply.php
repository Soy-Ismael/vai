<?php
// Este archivo php espera datos en formato json, aqui se establece la cabecera como application/json para que php sepa con que va a trabajar
header('Content-Type: application/json; charset=utf-8');

// Para recibir los datos del formulario y aplicarlos al archivo .json:
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    
    // Como los datos se envian en formato json es necesario obtenerlos de esta manera, entonces; si se recibe algo por post (y se espera que sea un json), haz esto: (el true me devuelve un array asociativo)
    $data = json_decode(file_get_contents('php://input'), true);

    //* Primer formulario
    // Si name es null o no tiene valor obtendra el valor de '' por defecto (??)
    $name = htmlspecialchars(trim($data['assistant']['name'] ?? ''));
    $language = htmlspecialchars(trim($data['assistant']['language'] ?? ''));
    $hourFormat = htmlspecialchars(trim($data['assistant']['hourFormat'] ?? ''));
    $voiceNumber = htmlspecialchars(trim($data['assistant']['voiceNumber'] ?? ''));
    $operativeSystem = htmlspecialchars(trim($data['assistant']['operativeSystem'] ?? ''));
    $role = htmlspecialchars(trim($data['assistant']['role'] ?? ''));
    // echo "Nombre" . $name;
    
    //* Segundo formulario
    $voiceEngine = htmlspecialchars(trim($data['env']['voiceEngine'] ?? ''));
    $encryption_phrase = htmlspecialchars(trim($data['env']['encryption_phrase'] ?? ''));
    $azureApiKey = htmlspecialchars(trim($data['env']['azureApiKey'] ?? ''));
    $openaiApiKey = htmlspecialchars(trim($data['env']['openaiApiKey'] ?? ''));
    $txtFilePath = trim($data['env']['txtFilePath'] ?? '');
    $port = htmlspecialchars(trim($data['env']['port'] ?? ''));
    $webAdminPassword = htmlspecialchars(trim($data['webAdminPassword'] ?? ''));
    
    //* Tercer formulario
    $playYtContent = htmlspecialchars(trim($data['modules']['playYtContent'] ?? ''));
    $searchInWeb = htmlspecialchars(trim($data['modules']['searchInWeb'] ?? ''));
    $infoInWeb = htmlspecialchars(trim($data['modules']['infoInWeb'] ?? ''));
    $reminders = htmlspecialchars(trim($data['modules']['reminders'] ?? ''));
    $jokes = htmlspecialchars(trim($data['modules']['jokes'] ?? ''));
    $excelReport = htmlspecialchars(trim($data['modules']['excelReport'] ?? ''));
    $sayHour = htmlspecialchars(trim($data['modules']['sayHour'] ?? ''));
    $timer = htmlspecialchars(trim($data['modules']['timer'] ?? ''));
    $whatDayWas = htmlspecialchars(trim($data['modules']['whatDayWas'] ?? ''));
    $checkAvailability = htmlspecialchars(trim($data['modules']['checkAvailability'] ?? ''));
    $sayName = htmlspecialchars(trim($data['modules']['sayName'] ?? ''));
    $requestConfigFile = htmlspecialchars(trim($data['modules']['requestConfigFile'] ?? ''));
    $createConfigFile = htmlspecialchars(trim($data['modules']['createConfigFile'] ?? ''));
    $closingPhrase = htmlspecialchars(trim($data['modules']['closingPhrase'] ?? ''));
    $wakeOnLan = htmlspecialchars(trim($data['modules']['wakeOnLan'] ?? ''));
    $webInterface = htmlspecialchars(trim($data['modules']['webInterface'] ?? ''));
    $aiModule = htmlspecialchars(trim($data['modules']['aiModule'] ?? ''));
    $countExecutionTime = htmlspecialchars(trim($data['modules']['countExecutionTime'] ?? ''));
    $printBanner = htmlspecialchars(trim($data['modules']['printBanner'] ?? ''));

    //* Tabla
    foreach ($data['wakeonlan']['mac'] as $key => $value) {
        
    }

    
    if (!empty($name)) {
        $response = [
            "status" => "success",
            'ok' => true,
            "code" => 200,
            "message" => "Operation was completed successfully.",
            "data"=> $data,
            'timestamp' => date('c'), // Marca de tiempo en formato ISO 8601
            "errors" => null
        ];
    } else {
        $response = [
            'status' => 'error',
            'ok' => false,
            'code' => 400,
            'message' => "name field can't be empty.",
            'data' => null,
            'errors' => [
                'Data was received, but there is an issue in the data'
            ]
        ];
    }
    // convierte el array respuesta a un json y la envia a javascript como respuesta de la petición
    echo json_encode($response);
    
    // Enviar los datos al archivo config.json en assets/config.json
    $json_for_humans = json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
    file_put_contents('assets/test.json', $json_for_humans);

    // Enviar una respuesta al usuario (por ejemplo, una página de confirmación)
    // header('Location: confirmation.php');
    // exit;
}
?>