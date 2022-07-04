from django.db import models

#  clases para los productos de la tienda


class Categoria(models.Model):
    idCategoria = models.IntegerField(
        primary_key=True, verbose_name='ID de Categoria')
    nombreCategoria = models.CharField(
        max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria


class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True, verbose_name='ID Producto')
    nombre = models.CharField(
        max_length=50, verbose_name='Nombre Producto', default="Producto para mascotas")
    marca = models.CharField(max_length=20, verbose_name='Marca Producto')
    categoria = models.ForeignKey(
        Categoria, default=1,  on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=500, verbose_name='Descripcion Producto')
    precio = models.PositiveIntegerField(default=10000)
    imagen = models.ImageField(
        upload_to='static/images/upload/', default='static/images/fundaciones/5.png')

    def __str__(self):
        return self.descripcion

# clases de peludos en adopcion adopcion


class TipoMascota(models.Model):
    idTipoMascota = models.AutoField(
        primary_key=True, verbose_name='ID de Mascota')
    descTipoMascota = models.CharField(
        max_length=15, verbose_name='Descripción de Mascota')

    def __str__(self):
        return self.descTipoMascota


class Raza(models.Model):
    idRaza = models.AutoField(primary_key=True, verbose_name='ID de Raza')
    descRaza = models.CharField(max_length=40, verbose_name='Descripción Raza')
    tipoMascota = models.ForeignKey(
        TipoMascota, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.descRaza


class Sexo(models.Model):
    idSexo = models.AutoField(primary_key=True)
    descSexo = models.CharField(max_length=15)

    def __str__(self):
        return self.descSexo


class Mascota(models.Model):
    idMascota = models.AutoField(
        primary_key=True, verbose_name='ID de Mascota')
    nombreMascota = models.CharField(
        max_length=40, verbose_name='Nombre de Mascota')
    edadAnioMascota = models.IntegerField(
        verbose_name='Edad en Años de Mascota')
    edadMesesMascota = models.IntegerField(
        verbose_name='Edad en Meses de Mascota')
    sexoMascota = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    estEstirizadoMascota = models.BooleanField(
        verbose_name='Estado Estirilización de Mascota')
    razaMascota = models.ForeignKey(Raza, on_delete=models.CASCADE)
    fotoMascota = models.ImageField(upload_to='static/images/upload/')

    def __str__(self):
        return self.nombreMascota


class Fundacion(models.Model):
    idFundacion = models.AutoField(
        primary_key=True, verbose_name='ID de Fundación')
    nombreFundacion = models.CharField(
        max_length=150, verbose_name='Fundación')
    descFundacion = models.CharField(
        max_length=500, verbose_name="Descripción de la Fundación")
    fotoFundacion = models.ImageField(
        upload_to='static/images/upload/', default='static/images/fundaciones/5.png')
    website = models.URLField(
        max_length=150, verbose_name='Pagina Web', default="https://todosdecidimos.org/animales/")

    def __str__(self):
        return self.nombreFundacion

# Cliente para guardar en la BD


class Cliente(models.Model):
    idCliente = models.AutoField(
        primary_key=True, verbose_name='ID de Cliente')
    nombreCliente = models.CharField(
        max_length=40, verbose_name='Nombre de Cliente')
    ApellidoCliente = models.CharField(
        max_length=40, verbose_name='Apellidos de Cliente')
    telefonoCliente = models.CharField(
        max_length=40, verbose_name='Telefono de Cliente')
    emailCliente = models.CharField(
        max_length=100, verbose_name='Email de Cliente')
    direccionCliente = models.CharField(
        max_length=250, verbose_name='Direccion de Cliente')
    RegionCliente = models.CharField(
        max_length=250, verbose_name='Region de Cliente')
    ComunaCliente = models.CharField(
        max_length=250, verbose_name='Comuna de Cliente')

    def __str__(self):
        return self.nombreCliente
