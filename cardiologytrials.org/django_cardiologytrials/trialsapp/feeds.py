from django.contrib.syndication.views import Feed
from trialsapp.models import Trial

class LatestTrialsFeed(Feed):
		title = "CardiologyTrials.org Latest Trials"
		link = "/"
		description = "The latest clinical trials in cardiology added to CardiologyTrials.org"
		
		def items(self):
			return Trial.objects.order_by('-pub_date')[:10]
			
		def item_title(self, item):
			return item.name
			
		def item_description(self, item):
			return item.treatment + " in " + item.problem		
			
class AllTrialsFeed(Feed):
		title = "CardiologyTrials.org Trials"
		link = "/"
		description = "The most important clinical trials in cardiology - CardiologyTrials.org"
		
		def items(self):
			return Trial.objects.order_by('name')
			
		def item_title(self, item):
			return item.name
			
		def item_description(self, item):
			return item.treatment + " in " + item.problem