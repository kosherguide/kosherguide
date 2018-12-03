$(document).ready(function() {

    // =====================================
    // = DETAIL CAROUSEL
    // =====================================

    $('.detailCarousel').slick({
        infinite: false,
        speed: 300,
        slidesToShow: 4,
        slidesToScroll: 4,
    });

    // =====================================
    // = GALLERY SIMPLE LIGHTBOX
    // =====================================

    $('.imageGallery a').simpleLightbox({ fileExt: false });

}); //END READY