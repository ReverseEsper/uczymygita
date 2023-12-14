$(document).ready(function () {
    $("#startEc2Button").on("click", function () {
        // Wysyłanie żądania do API Gateway
        $.ajax({
            url: "https://68naws0d35.execute-api.eu-central-1.amazonaws.com/scenajakas/mclambda",  // Podmieńić to na rzeczywisty endpoint
            method: "GET",
            success: function (data) {
                alert("Instancja EC2 uruchomiona pomyślnie!");
            },
            error: function (error) {
                alert("Wystąpił błąd podczas uruchamiania instancji EC2.");
                console.error(error);
            }
        });
    });
    $("#stopEc2Button").on("click", function () {
        // Wysyłanie żądania do API Gateway
        $.ajax({
            url: "https://68naws0d35.execute-api.eu-central-1.amazonaws.com/scenajakas/mclambastop",  // Podmieńić to na rzeczywisty endpoint
            method: "GET",
            success: function (data) {
                alert("wylaczona");
            },
            error: function (error) {
                alert("Wystąpił błąd ");
                console.error(error);
            }
        });
    });
});
