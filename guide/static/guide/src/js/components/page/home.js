$(document).ready(function() {

    // =====================================
    // = DETAIL CAROUSEL
    // =====================================

    var detailCarousel = $('.owl-carousel.detailCarousel');
    detailCarousel.owlCarousel({
        loop: false,
        items: 4,
        margin: 10,
        stagePadding: 1,
        nav: true,
        dots: false,
        navText: ['', ''],
        navClass: ['icon icon-arrow_left', 'icon icon-arrow_right'],
        responsiveClass: true,
        responsive: {
            320: {
                items: 1
            },
            480: {
                items: 2
            },
            767: {
                items: 3
            },
            1279: {
                items: 4
            },
            1280: {
                items: 4
            }
        }
    });
    detailCarousel.owlCarousel();
    // detailCarousel.on('changed.owl.carousel', function(event) {
    //     event.preventDefault();
    //
    //     var items = event.item.count;
    //     var item  = event.item.index;
    //     var size  = event.page.size;
    //     var position = (parseInt(items) - parseInt(size));
    //
    //     (item != 0) ? detailCarousel.addClass('shadowL') :  detailCarousel.removeClass('shadowL');
    //     (item != position) ? detailCarousel.addClass('shadowR') :  detailCarousel.removeClass('shadowR');
    // });
    
    // // =====================================
    // // = TAB HOME MARKET
    // // =====================================
    //
    // $('.mr_menu li a').on('click', function (event) {
    //     event.preventDefault();
    //
    //     $('.mr_menu li a, [id ^= "mProduct_"]').removeClass('active');
    //     $(this).addClass('active');
    //     $(this.hash).addClass('active');
    // });

    
}); //END READY