from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
	user = models.ForeignKey(User)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	mobile = models.CharField(max_length=10)
	alternate_number = models.CharField(max_length=10, blank=True, null=True)

	def __unicode__(self):
		return self.first_name