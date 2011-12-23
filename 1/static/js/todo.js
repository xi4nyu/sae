/*

   Author: llq<llq17501@gmail.com>
   */

$(function(){
    var docKey = KeyBind();
    $(document).keypress(docKey);

    docKey.map(["a", "A"],function(){
        var x =$("#text_dialog").css("display") =="none"||$("#text_dialog").parent().css("display")=="none";
        if(x){
            $("#text_dialog").dialog();
            $("#add_text").focus();
            $("#add_text").val("");
        }
    });
    docKey.map(["j"], function(){
        if(select_id < id_num - 1){
            $(".todo_item:eq("+select_id+")").removeClass("select_item");
            select_id++;
            $(".todo_item:eq("+select_id+")").addClass("select_item");
        }
    });
    docKey.map(["k"], function(){
        if(select_id > 0 ){
            $(".todo_item:eq("+select_id+")").removeClass("select_item");
            select_id--;
            $(".todo_item:eq("+select_id+")").addClass("select_item");
        }
    });
    docKey.map(["d"], function(){
        var id=$("#todo_list .select_item").attr("id").replace("todo_item_","");
        $.post("/todo/del",{id:id},list_to_html);
    });
    docKey.map(["c"], function(){
        var item = $("#todo_list .select_item");
        var id = item.attr("id").replace("todo_item_","");
        var status;
        if(item.parents(".todo").length>0){
            status=2;
        }else if(item.parents(".done").length>0){
            status=1;
        }
        if(status){
            $.post("/todo/modify",{id:id,status:status},list_to_html);
        }
    });
    var textKey = KeyBind();
    textKey.map(["enter"], add_todo);
    textKey.map(["esc"], function(){
        $("#text_dialog").dialog("close");
    });
    $("#add_text").keydown(textKey);


    $("#text_dialog").hide();
    function get_select_id(hash){
        hash=hash?hash:location.hash;
        if(!hash || hash=="#")return 0;
        return hash.substring(1)-0;
    }
    var select_id=get_select_id();
    var id_num;
    function list_to_html(data){
        $("#todo_list .todo,#todo_list .done").empty();
        id_num=0;
        for(var i=0;i<data.result.length;i++){
            var tempstr="<div class='todo_item' id='todo_item_"+i+"' ><span class='item_text'>"+data.result[i].text+"</span></div>";
            if(data.result[i].status===1){
                id_num++;
                $("#todo_list .todo").append(tempstr);
            }else if(data.result[i].status===2){
                id_num++;
                $("#todo_list .done").append(tempstr);
            }
        }
        $(".todo_item:eq("+select_id+")").addClass("select_item");
    }
    function load_list(){
        $.get("/todo/list",list_to_html);
    }
    function add_todo(){
        $.post("/todo/add",{text:$("#add_text").val()},list_to_html);
        $("#add_text").val("");
    }
    load_list();
});
