/*
 * 弹出模态对话框
 *
 * author:          llq
 * email:           llq17501@163.com
 */

(function($){
    $(function(){
        var over = $("<div></div>");
        var pageHeight = document.body.clientHeight;
        over.addClass("overlay");
        over.keypress(function(e){
            if(e.keyCode == 27)
                over.hide();
        });
        $(document.body).append(over);
        over.hide();
        $.fn.dialog = function(option){
            var self = $(this);
            if(option == "close"){
                over.hide();
            }else{
                over.html(self);
                self.show();
                over.show();
                self.addClass("center");
                self.css("margin-top",(pageHeight-self.height())/2);
            }
        }
    });
})(jQuery);
