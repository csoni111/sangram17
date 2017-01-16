from django.db import models

class College(models.Model) :
	name = models.CharField(max_length=50)
	designation = models.CharField(max_length=50)
	college = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	mobile = models.CharField(max_length=10)
	mevents = models.ManyToManyField(MaleEvent)
	fevents = models.ManyToManyField(FemaleEvent)
	status = models.BooleanField(initial=False)

class MaleEvent(models.Model) :
	name = models.CharField(max_length=50)
	max_player = models.IntegerField("Max Players")

class FemaleEvent(models.Model) :
	name = models.CharField(max_length=50)
	max_player = models.IntegerField("Max Players")



