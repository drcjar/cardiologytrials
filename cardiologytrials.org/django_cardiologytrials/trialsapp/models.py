from django.db import models
from datetime import datetime

# Create your models here.
	
class Topic(models.Model):							# left-most column in the table
	name = models.CharField(max_length=200)
	displayname = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name
		
class Therapy(models.Model):						# 2nd column in the table
	name = models.CharField(max_length=200)
	displayname = models.CharField(max_length=200)
	topic = models.ForeignKey(Topic)
	def __unicode__(self):
		return self.topic.name + " / " + self.name

class Intervention(models.Model):					# 3rd column in the table
	name = models.CharField(max_length=200)
	displayname = models.CharField(max_length=200)
	therapy = models.ForeignKey(Therapy)
	def __unicode__(self):
		return self.therapy.__unicode__() + " / " + self.name

class Trial(models.Model):
	name = models.CharField(max_length=200)
	date = models.DateField()
	pub_date = models.DateTimeField(default=datetime.now, blank=True)
	problem = models.CharField(max_length=200)
	format = models.CharField(max_length=200,default='-')
	population = models.CharField(max_length=200)
	inclusion = models.TextField()
	exclusion = models.TextField()
	treatment = models.CharField(max_length=200)
	control = models.CharField(max_length=200)
	followup = models.CharField(max_length=200)
	primary_endpoint = models.TextField()
	secondary_endpoint = models.TextField()
	details = models.TextField(blank=True)
	brief_summary = models.CharField(max_length=200,blank=True)
	topic_therapy_intervention = models.ManyToManyField(Intervention)
	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return "/detail/%i/" % self.id

class Paper(models.Model):
	trial = models.ForeignKey(Trial)
	name = models.CharField(max_length=200)
	date = models.DateField()
	journal = models.CharField(max_length=200)
	pmid = models.CharField(max_length=200)
	benefit = models.IntegerField()
	benefit_details = models.TextField()
	def __unicode__(self):
		return self.journal
