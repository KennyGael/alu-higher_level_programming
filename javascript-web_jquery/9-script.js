$(document).ready(function () {
    $.getJSON("https://api.allorigins.win/get?url=" + encodeURIComponent("https://fourtonfish.com/hellosalut/?lang=fr"), function (data) {
        const jsonData = JSON.parse(data.contents); // Parse the response from the proxy
        $("DIV#hello").text(jsonData.hello); // Display the translated 'hello'
    });
});