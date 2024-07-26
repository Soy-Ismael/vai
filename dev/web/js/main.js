// Icono de "check" para indicar el estado del equipo con wake on lan
/* <i class="fa-solid fa-circle-check"></i>; */
// <i class="fa-regular fa-circle-check"></i>

// #e52e53 color opcional para icono de error o problema:
/* <i class="fa-solid fa-circle-info"></i>; */

const button = document.getElementById("sectionButton");

button.addEventListener('click', e => {
    e.preventDefault()
    alert("Modal - proximamente")
})