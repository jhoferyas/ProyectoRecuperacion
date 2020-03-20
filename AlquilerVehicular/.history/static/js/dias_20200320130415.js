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
            if (data != "") {
                var html = '';
                html += '<div class="col-md-12">';
                html += '<label>Propietario : </label>';
                html += '<input type="text"  class="form-control" value="' + data[0].user.fullName + '" readonly>';
                html += '</div>';
                $('#carData').html(html); //Se agreg el contenido a la tabla.
                $('#carro').val(data[0].cartId);
                //Y una vez construida la tabla aplican los cambios que realiza la librería.
            } else {
                alert("Vehiculo no registrado");
            }

        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log(textStatus);
        }
    });
}