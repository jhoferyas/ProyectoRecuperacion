$(document).ready(function() {

    $("#dias").val("0");
    $("#precio").val("0");
    $("#fechaini").change(function() {
        var b = $("#fechafin").val();
        console.log("Maldito inutil " + b);
        var a = $("#fechaini").val();
        console.log("Maldito inutil " + a);
        var fechaI = new Date(fechaInicial);
        var fechaF = new Date(fechaActual);
        var difM = fechaF - fechaI; // diferencia en milisegundos
        var difD = difM / (1000 * 60 * 60 * 24); // diferencia en dias
    });
    $("#fechafin").change(function() {

    });

});