from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from trialsapp.sitemap import *
from trialsapp.feeds import LatestTrialsFeed
from trialsapp.feeds import AllTrialsFeed
admin.autodiscover()

# a dictionary of sitemaps
sitemaps = {
	'main': MainSitemap,
    'trials': TrialSitemap,
	'acs': ACSSitemap,
	'af': AFSitemap,
	'cad': CADSitemap,
	'hf': HFSitemap,
	'htn': HTNSitemap,
	'intervention': InterventionSitemap,
	'lipids': LipidsSitemap,
	'surgery': SurgerySitemap,	
}

urlpatterns = patterns('',
	
	url(r'^admin/', include(admin.site.urls)),
	
	(r'^$', 'trialsapp.views.index'),
	
	(r'^detail/(?P<trial_id>\d+)/$', 'trialsapp.views.detail'),
	
	(r'^short/(?P<trial_id>\d+)/$', 'trialsapp.views.short'),
	
	(r'^acs/', 'trialsapp.views.acs'),
	(r'^af/', 'trialsapp.views.af'),
	(r'^cad/', 'trialsapp.views.cad'),
	(r'^hf/', 'trialsapp.views.hf'),
	(r'^htn/', 'trialsapp.views.htn'),
	(r'^intervention/', 'trialsapp.views.intervention'),
	(r'^lipids/', 'trialsapp.views.lipids'),
	(r'^surgery/', 'trialsapp.views.surgery'),
	
	(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nAllow: /", mimetype="text/plain")),
	
	(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
	
	(r'^feeds/latest/rss\.xml$', LatestTrialsFeed()),
	
	(r'^feeds/all/rss\.xml$', AllTrialsFeed()),
	
	#(r'^newdesign/', 'trialsapp.views.newdesign'),

)
