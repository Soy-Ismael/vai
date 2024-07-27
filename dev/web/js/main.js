// Icono de "check" para indicar el estado del equipo con wake on lan
/* <i class="fa-solid fa-circle-check"></i>; */
// <i class="fa-regular fa-circle-check"></i>

// #e52e53 color opcional para icono de error o problema:
/* <i class="fa-solid fa-circle-info"></i>; */

const addDevice = document.getElementById('sectionButton');
const table = document.getElementById('table');


addDevice.addEventListener('click', e => {
    e.preventDefault()
    alert("Modal - proximamente")
})

// console.log(table.children[1]);
fetch("http://localhost/web/assets/config.json")
    .then((response) => response.json())
    .then((data) => {
        const devices = data.wakeonlan.mac;
        const fragment = document.createDocumentFragment()
        // console.log(table.children[1]);
        Object.keys(devices).forEach(element => {
            const tr = document.createElement('TR');
            const tdName = document.createElement("TD");
            const tdIp = document.createElement("TD");
            const tdMac = document.createElement("TD");
            const tdStatus = document.createElement("TD");
            const tdActions = document.createElement("TD");
            
            tr.classList.add('table__row')
            tdName.classList.add("table__td");
            tdIp.classList.add("table__td");
            tdMac.classList.add("table__td");
            tdStatus.classList.add("table__td");
            tdActions.classList.add("table__td");

            tdStatus.classList.add('status');
            tdActions.classList.add('table__td--icons');

            tdName.textContent = `${devices[element].name}`.toUpperCase();
            tr.append(tdName) // required

            tdIp.textContent = `${devices[element].ip == "" ? 'N/A' : devices[element].ip}`
            tr.append(tdIp)

            if (devices[element].status == true){
                tdMac.textContent = `${devices[element].mac}`
                tr.append(tdMac);

                tdStatus.setAttribute('data-status', "true")
                tdStatus.innerHTML = '<i class="fa-solid fa-circle-check"></i>';
                tr.append(tdStatus)
            }else{
                tdMac.textContent = "N/A";
                tr.append(tdMac);

                tdStatus.setAttribute('data-status', "false")
                tdStatus.innerHTML = '<i class="fa-solid fa-circle-info"></i>';
                tr.append(tdStatus)
            }
            let customStyle = 'style="font-weight: 100;"'
            tdActions.innerHTML =
                `<i class="fa-solid fa-clipboard table__copy" ${customStyle}></i> <i class="fa-solid fa-pen-to-square table__edit" ${customStyle}></i> <i class="fa-solid fa-trash-can table__trash" ${customStyle}></i>`;
            tr.append(tdActions)
            fragment.append(tr)
        });
        table.children[1].appendChild(fragment)
    });