$(document).ready(function() {
    if ($("#fechaini").val() === "" || $("#fechafin").val() === "") {
        $("#dias").val("0");
        $("#precio").val("0");
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