from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from . import blocks

class HomePage(Page):
    author = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField("Post date", null=True, blank=True)
    config = models.CharField(max_length=255, default="default_config")

    content = StreamField([
        ("title_and_text", blocks.PageBlock(null=True, blank=True)),
        ('user', blocks.UserBlock(null=True, blank=True, icon='user')),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('content', classname="full"),
    ]
 
#  removing the security for testing purposes
@csrf_exempt 
def template_specifications(request):
    if request.method == "POST":
        print( 'JSON obj: "%s"' % request.body)
    return HttpResponse(request.body)
    # can return a template using TemplateResponse
