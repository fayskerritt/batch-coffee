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
    })
})
$(function () {
    $('.update-qty').change(function () {
        $(this).closest('.quantity-update').find('.update-button').removeClass('d-none');
        $(this).closest('.quantity-update').find('.update-button').addClass('d-block');
    })
})

$(function () {
    $('.cancel-button').click(function () {
        $(this).closest(".quantity-update").find('.update-button').removeClass('d-block');
        $(this).closest(".quantity-update").find('.update-button').addClass('d-none');
        window.location.reload();
    })
})