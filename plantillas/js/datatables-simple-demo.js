window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
         new simpleDatatables.DataTable(datatablesSimple, {
             language: {
                 url: "//cdn.datatables.net/plug-ins/1.11.4/i18n/es_es.json"
             }
         });

    }
});
