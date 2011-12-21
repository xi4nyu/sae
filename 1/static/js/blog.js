
$(function(){
    function publish_blog(){
        var content = $("#blog_content").val();
        var title = $("#blog_title").val();
        console.log(content);
        $.post("", {content:content, title: title}, publish_blog_callback);
    }
    function publish_blog_callback(data){
        console.log("publish", data);
    }
    $("#publish_blog").click(publish_blog);
});
