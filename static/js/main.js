$(document).ready(function () {
  'use strict'


  //cargar HTML siempre estando en el index
  // $('#logo').on('click', function () {
  //   $("#central").load('home');
  //   return false;
  // });
  // $('#div-btn0').on('click', function () {
  //   $('.navbar-nav li').removeClass('active');
  //   $("#central").load('home');
  //   return false;
  // });

  // $('#div-btn1').on('click', function () {
  //   $('.navbar-nav li').removeClass('active');
  //   $("#central").load('tienda');
  //   return false;
  // });

  // $('#div-btn2').on('click', function () {
  //   $('.navbar-nav li').removeClass('active');
  //   $("#central").load('nosotros');

  //   return false;
  // });

  // $('#div-btn3').on('click', function () {
  //   $('.navbar-nav li').removeClass('active');
  //   $("#central").load('contacto');
  //   return false;
  // });

  // $('#div-btn4').on('click', function () {
  //   $('.navbar-nav li').removeClass('active');
  //   $("#central").load('donaciones');
  //   return false;
  // });
  // $('#div-btn5').on('click', function () {
  //   $('.navbar-nav li').removeClass('active');
  //   $("#central").load('adopciones');
  //   return false;
  // });
  // $('#div-btn6').on('click', function () {
  //   $('.navbar-nav li').removeClass('active');
  //   $("#central").load('login');
  //   return false;
  // });
  // $('#div-btn7').on('click', function () {
  //   $('.navbar-nav li').removeClass('active');
  //   $("#central").load('perfil');
  //   return false;
  // });
  // $('#div-btn8').on('click', function () {
  //   $('.navbar-nav li').removeClass('active');
  //   $("#central").load('home');
  //   return false;
  // });



  //seccion para imagenes en carrusel, redireccionamiento sin cargar pagina 
  // $('#fotoTienda').on('click', function () {
  //   $("#central").load('tienda');
  //   return false;
  // });

  // $('#fotoNosotros').on('click', function () {
  //   $("#central").load('nosotros');
  //   return false;
  // });

  // $('#fotoContacto').on('click', function () {
  //   $("#central").load('contacto');
  //   return false;
  // });

  // $('#fotoDona').on('click', function () {
  //   $("#central").load('donaciones');
  //   return false;
  // });

  // $('#gatos').on('click', function () {
  //   $("#central").load('Gatos');
  //   return false;
  // });

  // $('#perros').on('click', function () {
  //   $("#central").load('Perros');
  //   return false;
  // });

  // $('#mas').on('click', function () {
  //   $("#central").load('Mas..');
  //   return false;
  // });

  // $('#btn-donacion').on('click', function () {
  //   $("#central").load('adopciones');
  //   return false;
  // });


  //Conexion para obtener los datos de comuna y regiones
  $.ajax({
    type: 'GET',
    url: 'https://apis.digital.gob.cl/dpa/regiones',
    dataType: 'json',
    success: function (data) {
      let iRegion = 0;
      let htmlRegion = '<option selected disabled value="sin-region">Seleccione región</option><option disabled value="sin-region">--</option>';
      $.each(data, function () {
        htmlRegion = htmlRegion + '<option value="' + data[iRegion].codigo + '">' + data[iRegion].nombre + '</option>';
        iRegion++;
      });
      $('#regiones').html(htmlRegion);

      $("#regiones").change(function () {
        let regionVal = $("#regiones").val();
        console.log(regionVal);
        $.ajax({
          type: 'GET',
          url: `https://apis.digital.gob.cl/dpa/regiones/${regionVal}/comunas`,
          dataType: 'json',
          success: function (data) {
            let iComuna = 0;
            let htmlComuna = '<option selected disabled value="sin-comuna">Seleccione región</option><option disabled value="sin-comuna">--</option>';
            $.each(data, function () {
              htmlComuna = htmlComuna + '<option value="' + data[iComuna].nombre + '">' + data[iComuna].nombre + '</option>';
              iComuna++;
            });
            $('#comunas').html(htmlComuna);
          }
        });
      });
    }
  });

  //Seccion de validacion de formulario
  $("#envio").on("click", function () {
    if ($("#nombre").val() == "") {
      event.preventDefault();
      $("#nombre").addClass("is-invalid");
      $("#nombre").change(function () {
        $("#nombre").removeClass("is-invalid");
        $("#nombre").addClass("is-valid");
      });
    } else {
      $("#nombre").addClass("is-valid");
    }
    if ($("#apellido").val() == "") {
      event.preventDefault();
      $("#apellido").addClass("is-invalid");
      $("#apellido").change(function () {
        $("#apellido").removeClass("is-invalid");
        $("#apellido").addClass("is-valid");
      });
    } else {
      $("#apellido").addClass("is-valid");
    }
    if ($("#tel").val() == "" || !$("#tel").val().includes("+569") || $("#tel").val().length < 12) {
      event.preventDefault();
      $("#tel").addClass("is-invalid");
      $("#tel").change(function () {
        $("#tel").removeClass("is-invalid");
      });
    } else {
      $("#tel").addClass("is-valid");
    }
    if ($("#email").val() == "" || !validateEmail($("#email").val())) {
      event.preventDefault();
      $("#email").addClass("is-invalid");
      $("#email").change(function () {
        $("#email").removeClass("is-invalid");
      });
    } else {
      $("#email").addClass("is-valid");
    }
    if ($("#Direccion").val() == "") {
      event.preventDefault();
      $("#Direccion").addClass("is-invalid");
      $("#Direccion").change(function () {
        $("#Direccion").removeClass("is-invalid");
        $("#Direccion").addClass("is-valid");
      });
    } else {
      $("#Direccion").addClass("is-valid");
    }
    if ($("#regiones").val() == "" || $("#regiones").val() == null) {
      event.preventDefault();
      $("#regiones").addClass("is-invalid");
      $("#regiones").change(function () {
        $("#regiones").removeClass("is-invalid");
        $("#regiones").addClass("is-valid");
      });
    } else {
      $("#regiones").addClass("is-valid");
    }
    if ($("#comunas").val() == "" || $("#comunas").val() == null) {
      event.preventDefault();
      $("#comunas").addClass("is-invalid");
      $("#comunas").change(function () {
        $("#comunas").removeClass("is-invalid");
        $("#comunas").addClass("is-valid");
      });
    } else {
      $("#comunas").addClass("is-valid");
    }

    //Mensaje confirmando formulario completado en base a cantidad de elementos validos
    let formValidos = document.querySelectorAll(".is-valid");
    if (formValidos.length == 7) {
      alert("Formulario completado con exito, pronto nos pondremos en contacto, Gracias!!")
    }
  });


  //funcion para validar el email
  function validateEmail(email) {
    let caract = new RegExp(/^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/);
    if (caract.test(email) == false) {
      return false;
    } else {
      return true;
    }
  }
});

