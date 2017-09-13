from django.db import models
from django.contrib.auth.models import User
from unittest.util import _MAX_LENGTH

class City(models.Model):
	city_name = models.CharField(max_length=20)
	created_by = models.CharField(max_length=255)
    	created_on = models.DateTimeField(auto_now_add=True)
    	modified_by = models.CharField(max_length=255)
    	modified_on = models.DateTimeField(auto_now=True)
    	is_active = models.BooleanField(default=True)

class Junction(models.Model):
	STATUS_TYPE = (('3', "GREEN"),
				   ('4', "AMBER"))
	SIGNAL = (('1', "OFF"),
			  ('2', "BLINKER"),
			  ('3', "SIGNAL"))
	MODE = (('02', "AUTO"),
			('03', "MANUAL"))

	junction_name = models.CharField(max_length=20)
	city = models.ForeignKey(City)
    	hour = models.IntegerField()
    	minute = models.IntegerField()
    	second = models.IntegerField()
    	day = models.IntegerField()
    	month = models.IntegerField()
    	year = models.IntegerField()
    	phase_no = models.IntegerField()
    	status = models.CharField(max_length=10, choices=STATUS_TYPE)
    	normal_time = models.IntegerField()
    	step_elased_time = models.IntegerField()
    	cycle_elased_time1 = models.IntegerField()
    	cycle_elased_time2 = models.IntegerField()
    	working_on = models.CharField(max_length=10, choices=SIGNAL)
    	mode = models.CharField(max_length=10, choices=SIGNAL)
    	total_cycle_time1 = models.CharField(max_length=10, choices=MODE)
    	total_cycle_time2 = models.IntegerField()
    	created_by = models.CharField(max_length=255)
    	created_on = models.DateTimeField(auto_now_add=True)
    	modified_by = models.CharField(max_length=255)
    	modified_on = models.DateTimeField(auto_now=True)
    	is_active = models.BooleanField(default=True)