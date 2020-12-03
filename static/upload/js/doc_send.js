$(function (){ 
    $("#submit").on("click", function(){ ajax_send(); }); 
});

function ajax_send(){

    var fd          = new FormData( $("#upload_form").get(0) );

    $.ajax({
        url: "", 
        type: "POST",
        data: fd, 
        processData: false,
        contentType: false,
        dataType: 'json'
    }).done( function(data, status, xhr ) { 
        $("#content_area").html(data.content);
    }).fail( function(xhr, status, error) {
        console.log(status + ":" + error );
    }); 

}

