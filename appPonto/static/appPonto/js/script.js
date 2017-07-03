var nombre_boton_eliminar = ".add"; // Clase

    $(document).on('ready',function(){
        $(nombre_boton_eliminar).on('click',function(e){
            e.preventDefault();
            var Pid = $(this).attr('id');
            var name = $(this).data('name');
            $('#modal_idFrequencia').val(Pid);
            $('#modal_name').text(name);
        });
    });