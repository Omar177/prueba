$(document).on('ready',Iniciar);

function Iniciar()
{

	var iniciarSecion=$('#iniciarSecion');
	iniciarSecion.hide();
	
	var frmEstudiantes=$('#frmEstudiantes');
	frmEstudiantes.hide();


	var registrar=$('#registrarEstudiante');
	registrar.on('click',RegistrarEstudiantes);

	var iniciarSecion=$('#iniciarSecion');
	iniciarSecion.on('click', iniciarEstudiante);


	var iniciarSecion2=$('#iniciarSecion2');
	iniciarSecion2.hide();
	
	var frmEstudiantes2=$('#frmEstudiantes2');
	frmEstudiantes2.hide();


	var registrar2=$('#registrarEstudiante2');
	registrar2.on('click',RegistrarDocente);

	var iniciarSecion2=$('#iniciarSecion2');
	iniciarSecion2.on('click', iniciarDocente);


}



function iniciarEstudiante()
{
	var frmEstudiantes=$('#frmEstudiantes');
	frmEstudiantes.hide();

	var frmIniciarSesion=$('#frmIniciarSesion');
	frmIniciarSesion.show();

	var iniciarSecion=$('#iniciarSecion');
	iniciarSecion.hide();

	var registrar=$('#registrarEstudiante');
	registrar.show();
}

function RegistrarDocente()
{
	var frmEstudiantes2=$('#frmEstudiantes2');
	frmEstudiantes2.show();

	var frmIniciarSesion2=$('#frmIniciarSesion2');
	frmIniciarSesion2.hide();

	var registrar2=$('#registrarEstudiante2');
	registrar2.hide();

	var iniciarSecion2=$('#iniciarSecion2');
	iniciarSecion2.show();

}

function iniciarDocente()
{
	var frmEstudiantes2=$('#frmEstudiantes2');
	frmEstudiantes2.hide();

	var frmIniciarSesion2=$('#frmIniciarSesion2');
	frmIniciarSesion2.show();

	var iniciarSecion2=$('#iniciarSecion2');
	iniciarSecion2.hide();

	var registrar2=$('#registrarEstudiante2');
	registrar2.show();
}
