from django.db import models

# Create your models here.

class Nav_home(models.Model):
			id_nav_home = models.AutoField(db_column="idNavhome", primary_key=True)
			nav_home = models.CharField(max_length=20, blank=False, null=False)

			def __str__(self):
				return str(self.nav_home)
			
