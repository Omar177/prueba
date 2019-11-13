$(function () {
	/*$('#idproducto').change(function() {
		//alert($('#idproducto').val());
		$.ajax({
			type: 'POST',
			url: '/detalleventa/precio',
			data: {
				'idproducto' : $('#idproducto').val(),
				'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
			},
			success: precioSuccess,
			dataType: 'html'
		});
	});*/
	
	$('#idproducto').change(function() {
		//alert($('#idproducto').val());
		//console.log("Selecciono opciones");
		$value = $('#idproducto').val();
		$.ajax({
        type:"GET",
        url: '/App1/precio',
        data: {
          'codigo': $value
        },
        dataType: 'json',
        success: function (data) {
        console.log(data.existencia)
        $('#precio').val(data.existencia);
        }
      });
	});

	$('#id_cantidad_producto').keyup(function(e) {
		$cant = $(this).val();
		$precio = $('#precio').val();
		$('#id_precio_total').val($cant*$precio);
	});
});