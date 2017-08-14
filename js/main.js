$(function(){
    /*
     *锚点点击跳转
     */
    var href = "";
    var pos = 0;
    $(".side-tag a").click(function(e){
        $(".side-tag li").each(function () {
            $(this).removeClass("active");
        });
        $(this).parent("li").addClass("active");
        e.preventDefault();
        href = $(this).attr("href");
        pos = $(href).position().top - 60;
        $("html,body").animate({ scrollTop: pos }, 500);
    });
    $(".side-item.active").next().css("display", "block");

    
})