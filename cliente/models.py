from django.db import models

# Create your models here. 
class Nav_cliente(models.Model):
	id_nav_cliente = models.AutoField(db_column="idNavcliente", primary_key=True)
	nav_cliente = models.CharField(max_length=20, blank=False, null=False)
	url_cliente = models.CharField(max_length=100, default='default_value')
	def __str__(self):
		return str(self.nav_cliente)
