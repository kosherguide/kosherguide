$(document).ready(function() {
    // =====================================
    // = SHOW HAMBURGER MOBILE MENU
    // =====================================

    $('.hamburger').on('click', function (event) {
        event.preventDefault();
        var contFluid = $('.contFluid');
        var menu = $('.nav_mobile');
        var menuWidth = menu.outerWidth();
        var menuHeight = menu.outerHeight();

        $(this).toggleClass('is-active');

        if ($(this).is('.is-active')) {
            $('.mn__wrap.scrollable .viewport').css({'min-height': menuHeight + 'px'});
            $('body').css({"position": "fixed", "left": "0", "right": '0', "overflow": "hidden"});

            $('body').css({
                "-o-transform": "translate3d(" + menuWidth + "px, 0, 0)",
                "-ms-transform": "translate3d(" + menuWidth + "px, 0, 0)",
                "-moz-transform": "translate3d(" + menuWidth + "px, 0, 0)",
                "-webkit-transform": "translate3d(" + menuWidth + "px, 0, 0)",
                "transform": "translate3d(" + menuWidth + "px, 0, 0)"
            });
        } else {
            $('body').css({"position": "static"});

            $('body').css({
                "-webkit-transform": "translate3d(0, 0, 0)",
                "-moz-transform": "translate3d(0, 0, 0)",
                "-ms-transform": "translate3d(0, 0, 0)",
                "-o-transform": "translate3d(0, 0, 0)",
                "transform": "translate3d(0, 0, 0)"
            }).removeStyle('transform');
        }
    });

    $('.nm_menu li span').on('click', function () {
        var subcategory = $(this).siblings('.subcategory');
        subcategory.show();
        $('.nav_mobile').addClass('level_x2');
    });

    $('.nm_menu .back').on('click', function () {
        var $this = $(this);

        $('.nav_mobile').removeClass('level_x2');
        setTimeout(function () {
            $this.parent().hide()
        }, 500);
    });


    // =====================================
    // = POPUP GALLERY
    // =====================================

    $('.imageGallery a').simpleLightbox({fileExt: false});

}); //END READY
