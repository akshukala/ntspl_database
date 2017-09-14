from django.db import models
from django.contrib.auth.models import User
from unittest.util import _MAX_LENGTH

class City(models.Model):
	city_name = models.CharField(max_length=20)
	created_by = models.ForeignKey(User, null=True, blank=True, related_name="city_entered")
	created_on = models.DateTimeField(auto_now_add=True)
	modified_by = models.ForeignKey(User, null=True, blank=True, related_name="city_modified")
	modified_on = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)

class Junction(models.Model):
	junction_name = models.CharField(max_length=20)
	city = models.ForeignKey(City)
	created_by = models.ForeignKey(User, null=True, blank=True, related_name="junction_entered")
	created_on = models.DateTimeField(auto_now_add=True)
	modified_by = models.ForeignKey(User, null=True, blank=True, related_name="junction_modified")
	modified_on = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)

class Junction_data(models.Model):
	STATUS_TYPE = (('3', "GREEN"),
				   ('4', "AMBER"))
	SIGNAL = (('1', "OFF"),
			  ('2', "BLINKER"),
			  ('3', "SIGNAL"))
	MODE = (('02', "AUTO"),
			('03', "MANUAL"))

	junction = models.ForeignKey(Junction)
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
	created_by = models.ForeignKey(User, null=True, blank=True, related_name="junction_data_entered")
	created_on = models.DateTimeField(auto_now_add=True)
	modified_by = models.ForeignKey(User, null=True, blank=True, related_name="junction_data_modified")
	modified_on = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)