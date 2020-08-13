from django.db import models

class API(models.Model):
	""" Model for  the API as a whole """
	# The API Key
	key_hash = models.CharField(max_length=25)
	# A name for the API key
	name = models.CharField(max_length=25)
	# IP from where it was created
	ip = models.CharField(max_length=25)

class Screenshot(models.Model):
	""" This model is for the screenshots taken from ShareX """
	# The image itself
	img = models.BinaryField()
	# The image's MIME type
	mime = models.CharField(max_length=25)
	# The filename
	filename = models.CharField(max_length=25)
