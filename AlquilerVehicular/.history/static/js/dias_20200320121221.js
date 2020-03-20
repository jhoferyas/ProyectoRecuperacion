$(document).ready(function() {
    if ($("#fechaini").val() != null || $("#fechafin").val() != null) {
        $("#dias").val("0");
        $("#precio").val("0");
    } else {
        $("#fechaini").change(function() {
            var a = $("#fechaini").val();
            console.log("Maldito inutil " + a);
        });
        $("#fechafin").change(function() {
            var a = $("#fechafin").val();
            console.log("Maldito inutil " + a);
        });
    }
});