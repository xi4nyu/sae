$(function(){
    function login_callbak(data){
        data = $.parseJSON(data);
        if(data.success){
            document.location = data["data"]["back"];
        }else{
            $("#error_text").text("用户名或密码错误!");
        }
    }
    function login_click(){
        var user_name = $("#user_name").val(), password = $("#password").val();
        $.post("", {user_name : user_name, password: password}, login_callbak);
    }
    $("#btn_login").click(login_click);
    $("#password").keypress(KeyBind(["enter"], login_click));
});
