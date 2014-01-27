from django.contrib.comments.views.comments import post_free_comment
from django.http import Http404
import captcha
import settings

def free_comment_wrapper(request,extra_context={},context_processors=None):
    if request.POST:
        check_captcha = captcha.submit(request.POST.get('recaptcha_challenge_field',''), 
               request.POST.get('recaptcha_response_field',''), settings.RECAPTCHA_PRIVATE_KEY,   
               request.META['REMOTE_ADDR'])
        if check_captcha.is_valid is False:
            raise Http404, "Invalid Captcha Attempt"
        extra_context["recaptcha_html"]=captcha.displayhtml(settings.RECAPTCHA_PUB_KEY)
        return post_free_comment(request,extra_context,context_processors)
    raise Http404,"Only POSTs are allowed"

