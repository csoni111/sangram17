from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from registration.supplements.base import RegistrationSupplementBase

class MyRegistrationSupplement(RegistrationSupplementBase):

    realname = models.CharField("Real name", max_length=100, help_text="Please fill your real name")
    age = models.IntegerField("Age")
    remarks = models.TextField("Remarks", blank=True)

    def __str__(self):
        # a summary of this supplement
        return "%s (%s)" % (self.realname, self.age)	

# class College(models.Model) :
# 	name = models.CharField(max_length=50)
# 	designation = models.CharField(max_length=50)
# 	college = models.CharField(max_length=50)
# 	city = models.CharField(max_length=50)
# 	email = models.CharField(max_length=50)
# 	mobile = models.CharField(max_length=10)

# class MaleEvent(models.Model) :
# 	name = models.CharField(max_length=50)
# 	colleges = models.ForeignKey(College)

# class FemaleEvent(models.Model) :
# 	name = models.CharField(max_length=50)
# 	colleges = models.ForeignKey(College)



