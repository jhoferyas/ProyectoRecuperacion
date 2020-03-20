$(document).ready(function() {

    $("#dias").val("0");
    $("#precio").val("0");
    $("#fechaini").change(function() {
        var b = $("#fechafin").val();
        var a = $("#fechaini").val();
        if (b === "") {
            console.log("0")
        } else {
            var fechaI = new Date(a);
            var fechaF = new Date(b);
            var difM = fechaF - fechaI; // diferencia en milisegundos
            var difD = difM / (1000 * 60 * 60 * 24); // diferencia en dias
            console.log(difD);
            if (a === "") {
                console.log("0")
            }
        }

    });
    $("#fechafin").change(function() {
        var b = $("#fechafin").val();
        var a = $("#fechaini").val();
        if (a === "") {
            console.log("0")
        } else {
            var fechaI = new Date(a);
            var fechaF = new Date(b);
            var difM = fechaF - fechaI; // diferencia en milisegundos
            var difD = difM / (1000 * 60 * 60 * 24); // diferencia en dias
            console.log(difD);
        }
    });

});