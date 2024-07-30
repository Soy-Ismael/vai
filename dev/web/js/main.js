// Icono de "check" para indicar el estado del equipo con wake on lan
/* <i class="fa-solid fa-circle-check"></i>; */
// <i class="fa-regular fa-circle-check"></i>

// #e52e53 color opcional para icono de error o problema:
/* <i class="fa-solid fa-circle-info"></i>; */

const addDevice = document.getElementById('sectionButton');
const table = document.getElementById('table');

// Actions column
const copyButton = document.getElementById("copyButton");
const editButton = document.getElementById("editButton");
const deleteButton = document.getElementById("deleteButton");

const newName = document.getElementById("newName");
const newIp = document.getElementById("newIp");
const newMac = document.getElementById("newMac");

// Modal para editar
const editModal = document.getElementById('modal2');
const closeEditModal = document.getElementById('closeModal2');
const editDevice = document.getElementById("editDevice");

const editName = document.getElementById('editName');
const editIp = document.getElementById('editIp');
const editMac = document.getElementById('editMac');

if (location.pathname == "/web/configuration.php"){
    //* Código para enviar formulario
    const submitButton = document.getElementById("submitButton");

    submitButton.addEventListener("click", (e) => {
        sendData();
    });

    //* Rellenar tabla con las direcciones mac
    // console.log(table.children[1]);
    fetch("http://localhost/web/assets/config.json")
        .then((response) => response.json())
        .then((data) => {
            const devices = data.wakeonlan.mac;
            const fragment = document.createDocumentFragment();
            // console.log(table.children[1]);
            Object.keys(devices).forEach((element) => {
                const tr = document.createElement("TR");
                const tdName = document.createElement("TD");
                const tdIp = document.createElement("TD");
                const tdMac = document.createElement("TD");
                const tdStatus = document.createElement("TD");
                const tdActions = document.createElement("TD");

                tr.classList.add("table__row");
                tdName.classList.add("table__td");
                tdIp.classList.add("table__td");
                tdMac.classList.add("table__td");
                tdStatus.classList.add("table__td");
                tdActions.classList.add("table__td");

                tdStatus.classList.add("status");
                tdActions.classList.add("table__td--icons");

                tdName.textContent = `${devices[element].name}`.toUpperCase();
                tr.append(tdName); // required

                tdIp.textContent = `${
                    devices[element].ip == "" ? "N/A" : devices[element].ip
                }`;
                tr.append(tdIp);

                if (devices[element].status == true) {
                    tdMac.textContent = `${devices[element].mac}`;
                    tr.append(tdMac);

                    tdStatus.setAttribute("data-status", "true");
                    tdStatus.setAttribute("title", "Correcto");
                    tdStatus.innerHTML =
                        '<i class="fa-solid fa-circle-check"></i>';
                    tr.append(tdStatus);
                } else {
                    tdMac.textContent = "N/A";
                    tr.append(tdMac);

                    tdStatus.setAttribute("data-status", "false");
                    tdStatus.setAttribute("title", "Incorrecto");
                    tdStatus.innerHTML =
                        '<i class="fa-solid fa-circle-info"></i>';
                    tr.append(tdStatus);
                }
                let customStyle = 'style="font-weight: 100;"';
                tdActions.innerHTML = `<i class="fa-solid fa-clipboard table__copy" ${customStyle}></i> <i class="fa-solid fa-pen-to-square table__edit" ${customStyle}></i> <i class="fa-solid fa-trash-can table__trash" ${customStyle}></i>`;
                tr.append(tdActions);
                fragment.append(tr);
            });
            table.children[1].appendChild(fragment);
        });
}

const sendData = () =>{
    const form1Data = new FormData(document.getElementById("form1"));
    const form2Data = new FormData(document.getElementById("form2"));
    const form3Data = new FormData(document.getElementById("form3"));
    const allFormData = {
        assistant: {},
        env: {},
        modules: {},
        wakeonlan: {
            mac: {},
            index: {}
        }
    };

    form1Data.forEach((value, key) => {
        // allFormData[key] = value;
        allFormData.assistant[key] = value;
    });
    
    form2Data.forEach((value, key) => {
        allFormData.env[key] = value
    });
    
    form3Data.forEach((value, key) => {
        allFormData.modules[key] = Boolean(value);
    });

    let mac = {}
    let indexCounter = 1;

    for (const device of table.children[1].children) {
        const index = `pc${indexCounter}`;
        allFormData.wakeonlan.mac[index] = {
            'name' : device.children[0].textContent.toLowerCase(),
            'ip' : device.children[1].textContent == 'N/A' ? '' : device.children[1].textContent,
            'mac' : device.children[2].textContent == 'N/A' ? '' : device.children[2].textContent,
            'status': device.children[3].dataset.status == "false" ? false : true 
        }
        indexCounter++;
    }

    // console.log(JSON.stringify(allFormData));

    // Enviar datos al servidor usando AJAX - fetch
    fetch("http://localhost/web/apply.php", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(allFormData),
    })
    // Hay que hacer algunas modificaciones en lo que devuelve el servidor si se quiere trabajar con .json()
    .then((response) => {
        if(response.ok){
            return response.json()
        }else{
            // Lanza un error si no se pudo enviar el formulario, de este modo tambien funcionara para otros errores
            throw new Error('wrong path to resource')
        }
    })
    .then((data) => {
        sendReview("Formulario enviado con exito", true);

        // Los datos de respuesta del servidor
        console.log(data);
    })
    .catch((err) => {
        sendReview("Error al enviar el formulario", false);
        console.error(err);
    });
}

//* Modals
// message = mensaje a mostrar en formato string, isItPossitive es un booleano que pintara el cuadro de verde o rojo dependiendo de si el mensaje es positivo o negativo, true o false
const sendReview = (message, isItPositive) => {
    let color
    let backgroundColor
    
    color = '#fff'
    if (isItPositive){
        // color = 'inherit'
        backgroundColor = "#00A65A";
    }else{
        // color = '#fff'
        backgroundColor = "#FF2954";
    }
    
    const messageModal = document.getElementById("messageModal");

    messageModal.setAttribute("style", `background-color: ${backgroundColor}; color: ${color};`);
    messageModal.classList.add("show__custom__modal");
    messageModal.children[0].textContent = message;
    setTimeout(() => {
        messageModal.classList.remove("show__custom__modal");
    }, 3800);
}

// const openModal = document.getElementById('elemento_que_abrira_el_modal')
// const modal = document.getElementById('id_del_elemento_modal')
// const closeModal = document.getElementById('id_del_elemento_para_cerrar_el_modal')

// openModal.addEventListener('click', (e)=> {
//     // EL preventDefault previene que se muestre la almoadilla al presionar un link en caso de que estemos tratando con uno
//     e.preventDefault()
//     modal.classList.add("modal--show");
// })

// closeModal.addEventListener('click', (e)=> {
//     e.preventDefault()
//     modal.classList.remove("modal--show");
// })

//* Modal para solicitar información para añadir un nuevo equipo
const modal = document.getElementById('modal')
const closeModal = document.getElementById('closeModal')
const newDevice = document.getElementById('newDevice')

addDevice.addEventListener("click", e => {
    e.preventDefault();
    modal.classList.add("modal__custom--show");
});

closeModal.addEventListener('click', e => {
    e.preventDefault();
    modal.classList.remove("modal__custom--show");
})

newDevice.addEventListener("click", (e) => {
    e.preventDefault();
    table.children[1].appendChild(alterTable());
    // console.log(newName.value, newIp.value, newMac.value);
});

// Código para añadir un nuevo equipo (o editarlo) a partir del modal:
const alterTable = () => {
    const fragment = document.createDocumentFragment();
    // console.log(table.children[1]);
    const tr = document.createElement("TR");
    const tdName = document.createElement("TD");
    const tdIp = document.createElement("TD");
    const tdMac = document.createElement("TD");
    const tdStatus = document.createElement("TD");
    const tdActions = document.createElement("TD");

    tr.classList.add("table__row");
    tdName.classList.add("table__td");
    tdIp.classList.add("table__td");
    tdMac.classList.add("table__td");
    tdStatus.classList.add("table__td");
    tdActions.classList.add("table__td");

    tdStatus.classList.add("status");
    tdActions.classList.add("table__td--icons");

    // tdName.textContent = `${newName.value}`.toUpperCase();
    tdName.textContent = newName.value == "" ? "default" : newName.value;
    tr.append(tdName); // required

    tdIp.textContent = `${newIp.value == "" ? "N/A" : newIp.value}`;
    tr.append(tdIp);

    if (newMac.value != "") {
        tdMac.textContent = `${newMac.value}`;
        tr.append(tdMac);

        tdStatus.setAttribute("data-status", "true");
        tdStatus.setAttribute("title", "Correcto");
        tdStatus.innerHTML = '<i class="fa-solid fa-circle-check"></i>';
        tr.append(tdStatus);
    } else {
        tdMac.textContent = "N/A";
        tr.append(tdMac);

        tdStatus.setAttribute("data-status", "false");
        tdStatus.setAttribute("title", "Incorrecto");
        tdStatus.innerHTML = '<i class="fa-solid fa-circle-info"></i>';
        tr.append(tdStatus);
    }
    let customStyle = 'style="font-weight: 100;"';
    tdActions.innerHTML = `<i class="fa-solid fa-clipboard table__copy" ${customStyle}></i> <i class="fa-solid fa-pen-to-square table__edit" ${customStyle}></i> <i class="fa-solid fa-trash-can table__trash" ${customStyle}></i>`;
    tr.append(tdActions);
    fragment.append(tr);

    if (newName.value != "") {
        // Cerrar modal
        modal.classList.remove("modal__custom--show");

        // Devolver nuevo elemento
        // table.children[1].appendChild(fragment);
        return fragment
    } else {
        sendReview("El campo nombre no puede estar vacio", false);
    }
}


table.addEventListener('click', e => {
    if (e.target.classList[2] == "table__copy") {
        // Copiar
        navigator.clipboard.writeText(
            e.target.parentElement.parentElement.children[2].textContent
        );
        sendReview('Dirección mac copiada al portapapeles', true)
    }else if (e.target.classList[2] == "table__edit") {
        // Editar
        const parent = e.target.parentElement.parentElement;
        editModal.classList.add("modal__custom--show");

        editName.value = parent.children[0].textContent;
        editIp.value = parent.children[1].textContent == 'N/A' ? '' : parent.children[1].textContent;
        editMac.value = parent.children[2].textContent == 'N/A' ? '' : parent.children[2].textContent;

        console.log(parent);

        editDevice.addEventListener("click", (e) => {
            e.preventDefault();
            parent.children[1].textContent = editIp.value != "" ? editIp.value : 'N/A'
            
            if (editMac.value != "") {
                parent.children[2].textContent = editMac.value
                
                parent.children[3].setAttribute("data-status", "true");
                parent.children[3].setAttribute("title", "Correcto");
                parent.children[3].innerHTML = '<i class="fa-solid fa-circle-check"></i>';
            } else {
                parent.children[2].textContent = 'N/A'

                parent.children[3].setAttribute("data-status", "false");
                parent.children[3].setAttribute("title", "Incorrecto");
                parent.children[3].innerHTML = '<i class="fa-solid fa-circle-info"></i>';
            }

            if (editName.value != "") {
                // Cerrar modal
                parent.children[0].textContent = editName.value;
                editModal.classList.remove("modal__custom--show");
            } else {
                sendReview("El campo nombre no puede estar vacio", false);
            }
        });

        closeEditModal.addEventListener('click', (e) =>{
            e.preventDefault();
            editModal.classList.remove("modal__custom--show");
        })
        // parent.replace(parent, alterTable());
    } else if (e.target.classList[2] == "table__trash") {
        // Eliminar
        e.target.parentElement.parentElement.remove()
    }
})