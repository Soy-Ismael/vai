<?php
// Para enviar los datos del formulario y aplicarlos al archivo .json

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = htmlspecialchars(trim($_POST['name']));
    echo "HOLA";

    // Enviar los datos al archivo config.json en assets/config.json

    // Enviar una respuesta al usuario (por ejemplo, una página de confirmación)
    header('Location: confirmation.php');
    exit;
}
// <form method="post" action="htmlspecialchars($_SERVER['PHP_SELF']);">
// <input type="submit" name="submit" value="Enviar">
?>