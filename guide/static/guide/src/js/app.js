//= components/plugin/slick.js
//= components/plugin/simple-lightbox.js
//= components/plugin/mapbox.js
//= components/plugin/scrollbar.js

//= components/page/detail.js
//= components/page/map.js

function buttonUp() {
    let input = $('.sb-search-input');
    let submit = $('.sb-search-submit');

    let value = input.val();
    value = $.trim(value).length;
    if (value !== 0) {
        submit.css('z-index', '99');
    } else {
        input.val('');
        submit.css('z-index', '-999');
    }
}

$(document).ready(function() {

    // =====================================
    // = FORM SEARCH
    // =====================================

    let submitIcon = $('.sb-icon-search');
    let submitInput = $('.sb-search-input');
    let searchBox = $('.mn__search');
    let isOpen = false;

    $(document).mouseup(function () {
        if (isOpen == true) {
            submitInput.val('');
            $('.sb-search-submit').css('z-index', '-999');
            submitIcon.click();
        }
    });

    submitIcon.mouseup(function () {
        return false;
    });

    searchBox.mouseup(function () {
        return false;
    });

    submitIcon.click(function () {
        if (isOpen == false) {
            searchBox.addClass('sb-search-open');
            isOpen = true;
        } else {
            searchBox.removeClass('sb-search-open');
            isOpen = false;
        }
    });


    // =====================================
    // = CHANGE GRID
    // =====================================

    let gridPanel = $('.gridPanel span');

    gridPanel.on('click', function (event) {
        let id = $(this).data('id');
        let idGrid = $(this).parent().data('grid');
        let grid = $('.items[data-grid="' + idGrid + '"]');

        gridPanel.removeClass('is-active');
        $(this).addClass('is-active');

        if (id === 0) {
            grid.addClass('news-th').removeClass('news-th-list');
        }
        if (id === 1) {
            grid.addClass('news-th-list').removeClass('news-th');
        }
    });
});