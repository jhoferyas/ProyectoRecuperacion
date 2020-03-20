$(document).ready(function() {
    buscar();
    $("#dias").val("0");
    $("#precio").val("0");
    $("#fechaini").change(function() {
        var b = $("#fechafin").val();
        var a = $("#fechaini").val();
        if (b === "") {
            $("#dias").val("0");
            $("#precio").val("0");
        } else {

            if (a === "") {
                $("#dias").val("0");
                $("#precio").val("0");
            } else {
                var fechaI = new Date(a);
                var fechaF = new Date(b);
                var difM = fechaF - fechaI; // diferencia en milisegundos
                var difD = difM / (1000 * 60 * 60 * 24); // diferencia en dias
                console.log(difD);
                $("#dias").val(difD);
                $("#precio").val("$ " + difD * 15);
            }
        }

    });
    $("#fechafin").change(function() {
        var b = $("#fechafin").val();
        var a = $("#fechaini").val();
        if (a === "") {
            $("#dias").val("0");
            $("#precio").val("0");
        } else {
            if (b === "") {
                $("#dias").val("0");
                $("#precio").val("0");
            } else {
                var fechaI = new Date(a);
                var fechaF = new Date(b);
                var difM = fechaF - fechaI; // diferencia en milisegundos
                var difD = difM / (1000 * 60 * 60 * 24); // diferencia en dias
                console.log(difD);
                $("#dias").val(difD);
                $("#precio").val("$ " + difD * 15);
            }
        }
    });

});

function buscar() {
    var url = "http://localhost:8000/vehiculo/busqueda/";
    //console.log(url);
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'JSON',
        async: true,
        success: function(data, textStatus, jqXHR) {
            console.log(data);
            var html = "<option>Seleccione un Cliente</option>";
            var opt = "<option>Seleccione placa</option>";
            $.each(data, function(i, item) {
                html += '<option value="" >' + item.nombre + ' ' + item.Apellido + '</option>';

                opt += '<option value="" >' + item.placa + ' </option>';
            });
            $("#nombre").html(html);
            $("#placa").html(opt);


        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log(textStatus);
        }
    });
}