function Aparecer(id = "") {

    var popup = document.getElementById(id);
    popup.classList.toggle('d-none')
}

function SweetDeleteCodigo(id, link = "") {

    var nombre = document.getElementById('nombre'+id).innerText;
    var codigo = document.getElementById('id'+id).innerText;

    Swal.fire({
        title: '¿Estás seguro de eliminar esta entrada?',
        icon: 'warning',
        text: nombre,
        showCancelButton: true,
        cancelButtonText:'Cancelar',
        confirmButtonColor: '#bb2d3b',
        cancelButtonColor: '#0b5ed7',
        confirmButtonText: 'Borrar Entrada'
    }).then((result) => {
        if (result.isConfirmed) {

            window.location.replace(link+codigo);

        }
    })

}

function SweetDeleteId(id, link = "") {

    var nombre = document.getElementById('nombre'+id).innerText;

    Swal.fire({
        title: '¿Estás seguro de eliminar esta entrada?',
        icon: 'warning',
        text: nombre,
        showCancelButton: true,
        cancelButtonText:'Cancelar',
        confirmButtonColor: '#bb2d3b',
        cancelButtonColor: '#0b5ed7',
        confirmButtonText: 'Borrar Entrada'
    }).then((result) => {
        if (result.isConfirmed) {

            window.location.replace(link+id);

        }
    })

}