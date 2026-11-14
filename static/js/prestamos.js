document.addEventListener("DOMContentLoaded", function () {
    const fechaPrestamo = document.getElementById("id_fecha_prestamo");
    const fechaVencimiento = document.getElementById("id_fecha_vencimiento");

    if (!fechaPrestamo || !fechaVencimiento) {
        return;
    }

    fechaPrestamo.addEventListener("change", function () {
        if (!fechaPrestamo.value) {
            return;
        }

        const fecha = new Date(fechaPrestamo.value + "T00:00:00");
        fecha.setDate(fecha.getDate() + 15);

        const anio = fecha.getFullYear();
        const mes = String(fecha.getMonth() + 1).padStart(2, "0");
        const dia = String(fecha.getDate()).padStart(2, "0");

        fechaVencimiento.value = `${anio}-${mes}-${dia}`;
    });
});