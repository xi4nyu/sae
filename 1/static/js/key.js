/*

   Author: llq<llq17501@gmail.com>
   */

var KeyBind = function(keys, func){
    var re = function(e){
        var code = e.which||e.keyCode;
        if(e.type == "keyup" || e.type == "keydown"){
            if(code >= 96 && code <=105)
                code = code - 48;
            if(!e.shiftKey && code>64 && code <=90)
                code += 32;
            if(e.shiftKey && code>=48 && code <=57)
                code = ([41, 33, 64, 35, 36, 37, 94, 38, 42, 40])[code-48];
        }
        var name;
        if(code>=33 && code <=126){
            name = String.fromCharCode(code);
        }
        var dict = {13:"enter",32:"space", 27:"esc", 8:"backspace", 9: "tab"};
        if(dict[code])
            name = dict[code];
        //console.log(e, e.type, e.which, e.keyCode);
        if(name && arguments.callee._fs && arguments.callee._fs[name]){
            arguments.callee._fs[name].call(this, e , name);
        }
    }
    re._fs = {};
    re.map = function(keys,func){
        for(var i=0; i< keys.length;i++){
            this._fs[keys[i]]=func;
        }
    };
    if(keys&&func){
        re.map(keys, func);
    }
    return re
};
//var k = KeyBind();
//var s = ",.<>/?;:'\"[]{}-_=+)(*&^%$#@!~`\\|1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".split('');
//s.push("enter", "space", "backspace", "esc", "tab");
//for(var i=0;i<s.length;i++){
//    (function(c){
//        k.map([c],function(){
//            console.log(c)
//        })
//    })(s[i])
//}
//$(document).keypress(k);
//$(document).keydown(k);
//$(document).keyup(k);
