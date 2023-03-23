/*..............................................................................................
... PARA VALIDAR LOS DATOS .....................................................................
.............................................................................................*/
var csrftoken =  $.cookie('csrftoken') ;                                /*  '{{csrf_token}}'  */
function csrfSafeMethod(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
/*..............................................................................................
... TODOS LOS CURSOS ..Metodos ajax:...........................................................
'beforeSend' se ejecuta antes de la llamada
'.always' se ejecuta siempre 
'.fail' permite realizar acciones cuando hubo un error y sus parametros son:
.fail(fuction(request, errorTipe, errorMessage (se muestra al usuario)---- los tipo de errores son 
	timeout (tiempo)   error(pag no disponible)   abort(fue abortada la peticion) 
	parseerror(cuando pedimos un obj json y nos envia algo que no puede convertirse en json)

$each me permite hacer algo para cada elemento obtenido

serilize()   entrega todos los valores del formuario uno a uno

valor = +$( "#id_querycom" ).val();  se coloca un + si queremos obtener un valor solo numerico
............................................................................................. */
$( "#boton_prod" ).click(function(){
	valor = $( "#id_querycom" ).val();
	respuestproducto(valor)
});
function respuestproducto(valor){
    $.ajax({
        beforeSend : function(xhr, settings){                
			if(!csrfSafeMethod(settings.type) && !this.crossDomain){
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		url : "/tienda/buscar_producto2/",
		type : "GET",
		cache: false,
		data : { valor : valor,},
		success : function(json){
            valor_retornado = "<h2 style='text-align:center;'>"+json[0].producto+"</h2>"+ "<img style='width:100%;' src='/media/" + json[0].ruta_imagen + "'/>"
            $('#contenedor_filtrado').html(valor_retornado);
            console.log(json[0].producto);
		},
		error : function(xhr, errmsg, err){
			console.log('Error en carga de respuesta');
		},
    });
}