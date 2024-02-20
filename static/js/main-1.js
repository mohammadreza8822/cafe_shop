(function ($) {
    "use strict";


    /* ==========================
    Sticky Header
   ==========================*/
    $(window).scroll(function () {
        var scroll = $(window).scrollTop();
        if (scroll >= 20) {
            $(".header__style").addClass("sticky");
        } else {
            $(".header__style").removeClass("sticky");
        }
    });

}(jQuery));