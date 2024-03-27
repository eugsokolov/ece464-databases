$(document).ready(function(){
    // Button click event
    $("#postButton").click(function(){
        // Data to be sent in the POST request
        var postData = {
            data: "Hello from jQuery!"
        };

        // Making the POST request
        $.ajax({
            type: "POST",
            url: "http://localhost:8888/post",  // Replace with your server endpoint
            data: postData,
            success: function(response){
                // Handle the successful response from the server
                $("#result").text("Request completed. Server response: " + response);
                console.log("Server response:", response);
            },
            error: function(error){
                // Handle any errors that occurred during the POST request
                console.error("Error:", error);
            }
        });
    });
});