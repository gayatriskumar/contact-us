$(document).on('submit', '#post-form',function(e){
    $.ajax({
        type:'POST',
        url:'{% url "create" %}',
        data:{
            name:$('#name').val(),
            email:$('#email').val(),
            phoneno:$('#phoneno').val(),
            description:$('#description').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success:function(json){
        document.getElementById("post-form").reset();

        },
        error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
    });
});
