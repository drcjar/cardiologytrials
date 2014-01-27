from django.shortcuts import render_to_response, get_object_or_404
from trialsapp.models import Trial,Topic
from django.template import RequestContext

def index(request):
	topics_list=Topic.objects.order_by('name')
	return render_to_response('trialsapp/cardio.html', {'topics_list':topics_list},context_instance=RequestContext(request))

def detail(request, trial_id):
	p = get_object_or_404(Trial, pk=trial_id)
	return render_to_response('trialsapp/detail.html', {'trial': p}, context_instance=RequestContext(request))
	
def short(request, trial_id):
	p = get_object_or_404(Trial, pk=trial_id)
	return render_to_response('trialsapp/short.html', {'trial': p}, context_instance=RequestContext(request))
	
def acs(request):
	topics_list=Topic.objects.filter(name='ACS')
	return render_to_response('trialsapp/acs.html', {'topics_list':topics_list},context_instance=RequestContext(request))
	
def af(request):
	topics_list=Topic.objects.filter(name='AF')
	return render_to_response('trialsapp/af.html', {'topics_list':topics_list},context_instance=RequestContext(request))
	
def cad(request):
	topics_list=Topic.objects.filter(name='CAD')
	return render_to_response('trialsapp/cad.html', {'topics_list':topics_list},context_instance=RequestContext(request))
	
def hf(request):
	topics_list=Topic.objects.filter(name='HF')
	return render_to_response('trialsapp/hf.html', {'topics_list':topics_list},context_instance=RequestContext(request))
	
def htn(request):
	topics_list=Topic.objects.filter(name='HTN')
	return render_to_response('trialsapp/htn.html', {'topics_list':topics_list},context_instance=RequestContext(request))
	
def intervention(request):
	topics_list=Topic.objects.filter(name='Intervention')
	return render_to_response('trialsapp/intervention.html', {'topics_list':topics_list},context_instance=RequestContext(request))
	
def lipids(request):
	topics_list=Topic.objects.filter(name='Lipids')
	return render_to_response('trialsapp/lipids.html', {'topics_list':topics_list},context_instance=RequestContext(request))
	
def surgery(request):
	topics_list=Topic.objects.filter(name='Surgery')
	return render_to_response('trialsapp/surgery.html', {'topics_list':topics_list},context_instance=RequestContext(request))