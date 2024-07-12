from django.db import models

# Create your models here.

class Nav_delivery(models.Model):
	id_nav_delivery = models.AutoField(db_column="idNavdelivery", primary_key=True)
	nav_delivery = models.CharField(max_length=20, blank=False, null=False)
	url_delivery = models.CharField(max_length=100, default='default_value')
	def __str__(self):
		return str(self.nav_delivery)