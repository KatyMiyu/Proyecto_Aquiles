from django.db import models

# Create your models here.

class Nav_administrador(models.Model):
	id_navbar_adm = models.AutoField(db_column="idNavAdm", primary_key=True)
	nav_adm = models.CharField(max_length=20, blank=False, null=False)
	url_adm = models.CharField(max_length=100, default='default_value')
	def __str__(self):
		return str(self.nav_adm)
	
class Proveedores_administrador(models.Model):
	id_proveedor_adm = models.AutoField(db_column="idProveedoresAdm", primary_key=True)
	nom_proveedor_adm = models.CharField(max_length=50, blank=False, null=False)
	platos_adm = models.CharField(max_length=100, blank=False, null=False)
	ofertas_adm = models.CharField(max_length=50, blank=False, null=False)
	def __str__(self):
		return str(self.nom_proveedor_adm)
	
class Platos_administrador(models.Model):
    id_platos_adm = models.AutoField(db_column="idPlatosAdm", primary_key=True)
    nom_platos_adm = models.CharField(max_length=50, blank=False, null=False)
    precio_platos_adm = models.CharField(max_length=20, blank=False, null=False)
    oferta_platos_adm = models.CharField(max_length=20, blank=False, null=False)
    detalles_platos_adm = models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
	    return str(self.nom_platos_adm)

class Convenios_administrador(models.Model):
	id_convenio_adm = models.AutoField(db_column="idConvenioAdm", primary_key=True)
	nom_convenio_adm = models.CharField(max_length=50, blank=False, null=False)
	platos_convenio_adm = models.CharField(max_length=50, blank=False, null=False)
	modo_entrega = models.CharField(max_length=50, blank=False, null=False)
	def __str__(self):
	    return str(self.nom_convenio_adm)
	
class Estadisticas_administrador(models.Model):
	id_estadisticas = models.AutoField(db_column="idEstadisticas", primary_key=True)
	ventas_mes = models.CharField(max_length=50, blank=False, null=False)
	productos_vendidos = models.CharField(max_length=1000, blank=False, null=False)
	def __str__(self):
	    return str(self.ventas_mes)