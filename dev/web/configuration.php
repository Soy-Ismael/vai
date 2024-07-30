<?php include 'header.php'; ?>
    <main class="main">
        <h2 class="main__title">Configuración</h2>
        <section class="section">
            <h3 class="section__title">asistente</h3>
            <form action="" method="" class="form" id="form1">
                <!-- form: Especifica a qué formulario pertenece el campo de entrada, incluso si está fuera del elemento <form>. -->

                <!-- name input type: text -->
                <!-- language input type: combobox -->
                <!-- hour_format input type: combobox -->
                <!-- voice_number hard decision -->
                <!-- operative_system disable: take from useraggent -->
                <!-- voice_engine combobox -->
                <!-- role input: text -->
                <div class="form__field">
                    <label for="name">Nombre del asistente:</label>
                    <input type="text" name="name" id="name" class="form__input" placeholder="jarvis">
                </div>
                <div class="form__field">
                    <label for="language">Idioma:</label>
                    <input type="text" name="language" id="language" class="form__input" placeholder="es-ES">
                </div>
                <div class="form__field">
                    <label for="hourFormat">Formato de hora:</label>
                    <input type="text" name="hourFormat" id="hourFormat" class="form__input" placeholder="12">
                </div>
                <div class="form__field">
                    <label for="voiceNumber">Indice de voz:</label>
                    <input type="text" name="voiceNumber" id="voiceNumber" class="form__input" placeholder="0">
                </div>
                <div class="form__field">
                    <label for="operativeSystem">Sistema operativo:</label>
                    <input type="text" name="operativeSystem" id="operativeSystem" class="form__input" placeholder="Linux / Windows">
                </div>
                <div class="form__field">
                    <label for="role">Rol del asistente:</label>
                    <input type="text" name="role" id="role" class="form__input" placeholder="Eres maestro de programación">
                </div>
                <!-- <input type="submit" value="Enviar"> -->
            </form>
        </section>
        <section class="section">
            <h3 class="section__title">Entorno</h3>
            <form action="" method="" class="form" id="form2">
                <div class="form__field">
                    <label for="voiceEngine">Motor de voz:</label>
                    <input type="text" name="voiceEngine" id="voiceEngine" class="form__input" placeholder="pyttsx3 / azure">
                </div>
                <div class="form__field">
                    <label for="encryption_phrase">Frase de encriptado:</label>
                    <input type="text" name="encryption_phrase" id="encryption_phrase" class="form__input" placeholder="fresas">
                </div>
                <div class="form__field">
                    <label for="azureApiKey">Azure api key:</label>
                    <input type="text" name="azureApiKey" id="azureApiKey" class="form__input" placeholder="micr-45ksgts3...">
                </div>
                <div class="form__field">
                    <label for="openaiApiKey">OpenAI api key:</label>
                    <input type="text" name="openaiApiKey" id="openaiApiKey" class="form__input" placeholder="sk-45sTwb...">
                </div>
                <div class="form__field">
                    <label for="txtFilePath">ruta a los archivos txt:</label>
                    <input type="text" name="txtFilePath" id="txtFilePath" class="form__input" placeholder="/home/ubuntu/Desktop/">
                </div>
                <div class="form__field">
                    <label for="port">Puerto:</label>
                    <input type="text" name="port" id="port" class="form__input" placeholder="2625">
                </div>
                <div class="form__field">
                    <label for="webAdminPassword">Contraseña web:</label>
                    <input type="text" name="webAdminPassword" id="webAdminPassword" class="form__input" placeholder="papiJose">
                </div>
            </form>
        </section>
        <section class="section">
            <h3 class="section__title">Modulos</h3>
            <form action="" method="" class="form" id="form3">
                <div class="form__field form__field--checkbox">
                    <span>Reproducir contenido en youtube:</span>
                    <label for="playYtContent" class="form__checkbox">
                        <input type="hidden" name="playYtContent" value="">
                        <input type="checkbox" name="playYtContent" id="playYtContent" checked class="form__input form__input--checkbox">
                        <span>Habilitar</span>
                    </label>
                </div>
                <div class="form__field form__field--checkbox">
                    <span>Buscar en la web:</span>
                    <label for="searchInWeb" class="form__checkbox">
                        <input type="hidden" name="searchInWeb" value="">
                        <input type="checkbox" name="searchInWeb" id="searchInWeb"  class="form__input form__input--checkbox">
                        <span>Habilitar</span>
                    </label>
                </div>
                <div class="form__field form__field--checkbox">
                    <span>Información en la web:</span>
                    <label for="infoInWeb" class="form__checkbox">
                        <input type="hidden" name="infoInWeb" value="">
                        <input type="checkbox" name="infoInWeb" id="infoInWeb" checked class="form__input  form__input--checkbox">
                        <span>Habilitar</span>
                    </label>
                </div>
                <div class="form__field form__field--checkbox">
                    <span>Recordatorios:</span>
                    <label for="reminders" class="form__checkbox">
                        <input type="hidden" name="reminders" value="">
                        <input type="checkbox" name="reminders" id="reminders" class="form__input form__input--checkbox">
                        <span>Habilitar</span>
                    </label>
                </div>
                <div class="form__field form__field--checkbox">
                    <span>Contar chistes:</span>
                    <label for="jokes" class="form__checkbox">
                        <input type="hidden" name="jokes" value="">
                        <input type="checkbox" name="jokes" id="jokes" checked class="form__input form__input--checkbox">
                        <span>Habilitar</span>
                    </label>
                </div>
                <div class="form__field form__field--checkbox">
                    <span>Reportes de excel:</span>
                    <label for="excelReport" class="form__checkbox">
                        <input type="hidden" name="excelReport" value="">
                        <input type="checkbox" name="excelReport" id="excelReport" class="form__input form__input--checkbox">
                        <span>Habilitar</span>
                    </label>
                </div>
                <div class="form__field form__field--checkbox">
                    <span>Informar hora:</span>
                    <label for="sayHour" class="form__checkbox">
                        <input type="hidden" name="sayHour" value="">
                        <input type="checkbox" name="sayHour" id="sayHour" checked class="form__input form__input--checkbox">
                        <span>Habilitar</span>
                    </label>
                </div>
                <div class="form__field form__field--checkbox">
                    <span>Temporizador:</span>
                    <label for="timer" class="form__checkbox">
                        <input type="hidden" name="timer" value="">
                        <input type="checkbox" name="timer" id="timer" class="form__input form__input--checkbox">
                        <span>Habilitar</span>
                    </label>
                </div>
                <div class="form__field form__field--checkbox">
                    <span>Que día fue:</span>
                    <label for="whatDayWas" class="form__checkbox">
                        <input type="hidden" name="whatDayWas" value="">
                        <input type="checkbox" name="whatDayWas" id="whatDayWas" class="form__input form__input--checkbox">
                        <span>Habilitar</span>
                    </label>
                </div>
                <div class="form__field form__field--checkbox">
                    <span>Informar disponibilidad:</span>
                    <label for="checkAvailability" class="form__checkbox">
                        <input type="hidden" name="checkAvailability" value="">
                        <input type="checkbox" name="checkAvailability" checked id="checkAvailability" class="form__input form__input--checkbox">
                        <span>Habilitar</span>
                    </label>
                </div>
                <div class="form__field form__field--checkbox">
                    <span>Preguntar por nombre:</span>
                    <label for="sayName" class="form__checkbox">
                        <input type="hidden" name="sayName" value="">
                        <input type="checkbox" name="sayName" id="sayName" checked class="form__input form__input--checkbox">
                        <span>Habilitar</span>
                    </label>
                </div>
                <div class="form__field form__field--checkbox">
                    <span>Leer archivo de configuración:</span>
                    <label for="requestConfigFile" class="form__checkbox">
                        <input type="hidden" name="requestConfigFile" value="">
                        <input type="checkbox" name="requestConfigFile" id="requestConfigFile" class="form__input form__input--checkbox">
                        <span>Habilitar</span>
                    </label>
                </div>
                <div class="form__field form__field--checkbox">
                    <span>Crear archivo de configuración:</span>
                    <label for="createConfigFile" class="form__checkbox">
                        <input type="hidden" name="createConfigFile" value="">
                        <input type="checkbox" name="createConfigFile" id="createConfigFile" class="form__input form__input--checkbox">
                        <span>Habilitar</span>
                    </label>
                </div>
                <div class="form__field form__field--checkbox">
                    <span>Frase de cierre:</span>
                    <label for="closingPhrase" class="form__checkbox">
                        <input type="hidden" name="closingPhrase" value="">
                        <input type="checkbox" name="closingPhrase" id="closingPhrase" class="form__input form__input--checkbox">
                        <span>Habilitar</span>
                    </label>
                </div>
                <div class="form__field form__field--checkbox">
                    <span>Wake on lan:</span>
                    <label for="wakeOnLan" class="form__checkbox">
                        <input type="hidden" name="wakeOnLan" value="">
                        <input type="checkbox" name="wakeOnLan" id="wakeOnLan" checked class="form__input form__input--checkbox">
                        <span>Habilitar</span>
                    </label>
                </div>
                <div class="form__field form__field--checkbox">
                    <span>Interfaz web:</span>
                    <label for="webInterface" class="form__checkbox">
                        <input type="hidden" name="webInterface" value="">
                        <input type="checkbox" name="webInterface" id="webInterface" checked class="form__input form__input--checkbox">
                        <span>Habilitar</span>
                    </label>
                </div>
                <div class="form__field form__field--checkbox">
                    <span>Inteligencia artificial:</span>
                    <label for="aiModule" class="form__checkbox">
                        <input type="hidden" name="aiModule" value="">
                        <input type="checkbox" name="aiModule" id="aiModule" checked class="form__input form__input--checkbox">
                        <span>Habilitar</span>
                    </label>
                </div>
                <div class="form__field form__field--checkbox">
                    <span>Calcular tiempo de ejecución:</span>
                    <label for="countExecutionTime" class="form__checkbox">
                        <input type="hidden" name="countExecutionTime" value="">
                        <input type="checkbox" name="countExecutionTime" checked id="countExecutionTime" class="form__input form__input--checkbox">
                        <span>Habilitar</span>
                    </label>
                </div>
                <div class="form__field form__field--checkbox">
                    <span>Banner:</span>
                    <label for="printBanner" class="form__checkbox">
                        <!-- <input type="hidden" name="printBanner" value=""> -->
                         <!-- interpreta el "disabled" como que el checkbox esta desmarcado y cuando php recibe los datos recibe el valor de 0, como este checkbox estara desabilitado para ser modificado su valor por defecto sera on -->
                        <input type="hidden" name="printBanner" value="on">
                        <input type="checkbox" name="printBanner" checked disabled id="printBanner" class="form__input form__input--checkbox">
                        <span>Habilitar</span>
                    </label>
                </div>
            </form>
        </section>
        <section class="section">
            <h3 class="section__title">Wake On Lan</h3>
            <table class="table" id="table">
                <thead>
                    <tr class="table__row table__row--head">
                        <th class="table__th">NOMBRE</th>
                        <th class="table__th">DIRECCION IP</th>
                        <th class="table__th">DIRECCIÓN MAC</th>
                        <th class="table__th">ESTADO</th>
                        <th class="table__th">ACCIÓN</th>
                    </tr>
                </thead>
                <tbody>
                </tbody>
            </table>
            <!-- aqui deberia ir diseño y configuracion de paginación -->
            <button type="button" class="section__button" id="sectionButton"><i class="fa-solid fa-plus section__icon"></i> <span>Añadir nuevo equipo</span></button>
        </section>
        <!-- formulario para registrar un nuevo equipo, el usuario debe ingresar la mac, la ip y la mascara de subred -->
        <!-- <form action="apply.php" method="post" class="form">    
            <input type="submit" value="">
        </form> -->
        <button type="submit" id="submitButton" class="submitButton">Guardar</button>
    </main>
<?php include 'imports.php' ?>


<!-- Contenido del tbody -->

<!-- Mensaje para cuando no hayan datos -->
<!-- <p style="text-aligh: center;">No hay datos</p> -->
    
<!-- <tr class="table__row">
    <td class="table__td">Pc1</td>
    <td class="table__td">N/A</td>
    <td class="table__td">DC-4A-3E-80-E4-5B</td>
    <td class="table__td status" data-status="false">Activo</td>
    <td class="table__td table__td--icons"><i class="fa-solid fa-clipboard table__copy"></i> <i class="fa-solid fa-pen-to-square table__edit"></i> <i class="fa-solid fa-trash-can table__trash"></i></td>
</tr>
<tr class="table__row">
    <td class="table__td">Pc1</td>
    <td class="table__td">N/A</td>
    <td class="table__td">DC-4A-3E-80-E4-5B</td>
    <td class="table__td status" data-status="true">Activo</td>
    <td class="table__td table__td--icons"><i class="fa-solid fa-clipboard table__copy"></i> <i class="fa-solid fa-pen-to-square table__edit"></i> <i class="fa-solid fa-trash-can table__trash"></i></td>
</tr> -->