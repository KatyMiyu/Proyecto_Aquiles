from django.db import models

# Create your models here.

class Nav_proveedores(models.Model):
	id_navbar = models.AutoField(db_column="idNavProveedores", primary_key=True)
	nav_proveedores = models.CharField(max_length=20, blank=False, null=False)
	url_proveedores = models.CharField(max_length=100, default='default_value')
	def __str__(self):
		return str(self.nav_proveedores)
	
class Informacion_proveedores(models.Model):
	id_informacion = models.AutoField(db_column="idInformacion", primary_key=True)
	nom_proveedor = models.CharField(max_length=50, blank=False, null=False)
	direccion_proveedor = models.CharField(max_length=100, blank=False, null=False)
	numero_proveedor = models.CharField(max_length=20, blank=False, null=False)
	tipo_servicio = models.CharField(max_length=50, blank=False, null=False)
	def __str__(self):
		return str(self.nom_proveedor)
	
class Platos_proveedores(models.Model):
    id_platos = models.AutoField(db_column="idPlatos", primary_key=True)
    nom_platos = models.CharField(max_length=50, blank=False, null=False)
    precio_platos = models.CharField(max_length=20, blank=False, null=False)
    oferta_platos = models.CharField(max_length=20, blank=False, null=False)
    detalles_platos = models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
	    return str(self.nom_platos)