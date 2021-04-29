$(function () {
    $('#shop').click(function () {
        if ($('#shop-nav').css('display') == 'none') {
            $('#shop-nav').removeClass('d-none');
        } else {
            $('#shop-nav').addClass('d-none');
        }
    });
});
$(function () {
    $('#search-dropdown').click(function () {
        if ($('#mobile-search-bar').css('display') == 'none') {
            $('#mobile-search-bar').removeClass('d-none');
        } else {
            $('#mobile-search-bar').addClass('d-none');
        }
    });
});