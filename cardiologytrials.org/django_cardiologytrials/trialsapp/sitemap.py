from django.contrib.sitemaps import Sitemap
from trialsapp.models import Trial
		
class MainSitemap(Sitemap):
	def items(self):
		return [self]
	
	location = "/"	
	changefreq = "weekly"
	priority = 0.5
	
class TrialSitemap(Sitemap):
	changefreq = "monthly"
	priority = 0.5
	
	def items(self):
		return Trial.objects.order_by('id')
		
	def lastmod(self, obj):
		return obj.pub_date
		
class ACSSitemap(Sitemap):
	def items(self):
		return [self]
	
	location = "/acs/"	
	changefreq = "weekly"
	priority = 0.5
	
class AFSitemap(Sitemap):
	def items(self):
		return [self]
	
	location = "/af/"	
	changefreq = "weekly"
	priority = 0.5
	
class CADSitemap(Sitemap):
	def items(self):
		return [self]
	
	location = "/cad/"	
	changefreq = "weekly"
	priority = 0.5
	
class HFSitemap(Sitemap):
	def items(self):
		return [self]
	
	location = "/hf/"	
	changefreq = "weekly"
	priority = 0.5
	
class HTNSitemap(Sitemap):
	def items(self):
		return [self]
	
	location = "/htn/"	
	changefreq = "weekly"
	priority = 0.5
	
class InterventionSitemap(Sitemap):
	def items(self):
		return [self]
	
	location = "/intervention/"	
	changefreq = "weekly"
	priority = 0.5
	
class LipidsSitemap(Sitemap):
	def items(self):
		return [self]
	
	location = "/lipids/"	
	changefreq = "weekly"
	priority = 0.5
	
class SurgerySitemap(Sitemap):
	def items(self):
		return [self]
	
	location = "/surgery/"	
	changefreq = "weekly"
	priority = 0.5