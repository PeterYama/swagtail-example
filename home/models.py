from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from modelcluster.fields import ParentalKey
from . import blocks
from django.shortcuts import render


class HomePage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [FieldPanel("intro", classname="full")]


class AdeviPage(Page):
    author = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField("Post date", null=True, blank=True)
    body = models.CharField(max_length=255, default="default_config")

    content = StreamField(
        [
            ("title_and_text", blocks.PageBlock(null=True, blank=True)),
            ("user", blocks.UserBlock(null=True, blank=True, icon="user")),
        ]
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("content", classname="full"),
    ]


class AdeviGalleryImage(Orderable):
    page = ParentalKey(
        AdeviPage, on_delete=models.CASCADE, related_name="gallery_images"
    )
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    caption = models.CharField(blank=True, max_length=250)
    panels = [
        ImageChooserPanel("image"),
        FieldPanel("caption"),
    ]


#  removing the security for testing purposes
@csrf_exempt
def template_specifications(request):
    if request.methoda == "POST":
        print('JSON obj: "%s"' % request.body)
    return HttpResponse(request.body)
    # can return a template using TemplateResponse
