from django import template
from trialsapp.models import Topic,Therapy,Intervention
from django.contrib.comments.models import Comment
from django.contrib.contenttypes.models import ContentType

register = template.Library()

def get_topic_rows(topic_chosen):
	mylist = Therapy.objects.filter(topic=topic_chosen)
	rowcount = 0
	for therapyx in mylist:
		rowcount += get_therapy_rows(therapyx)
	return rowcount

def get_therapy_rows(therapy_chosen):
        rowcount = Intervention.objects.filter(therapy=therapy_chosen).count()
        if rowcount == 0:
                rowcount = 1
        return rowcount


register.simple_tag(get_topic_rows)
register.simple_tag(get_therapy_rows)
