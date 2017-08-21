$(document).on('ready', function () {
    $(".add").on('click', function (e) {
        e.preventDefault();
        var id = $(this).attr('id');
        var name = $(this).data('name');
        $('#modal_idFrequencia').val(id);
        $('#modal_name').text(name);
    });
});

$(document).on('ready', function () {
    $(".add").on('click', function (e) {
        e.preventDefault();
        var id = $(this).attr('id');
        var name = $(this).data('name');
        $('#modal_id_frequencia').val(id);
        $('#modal_name').text(name);
    });
});
