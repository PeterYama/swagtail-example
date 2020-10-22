"""Streamfields live in here."""

from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.blocks import StructValue
from wagtail.images.blocks import ImageChooserBlock

class LinkStructValue(StructValue):
    def url(self):
        external_url = self.get('external_url')
        page = self.get('page')
        if external_url:
            return external_url
        elif page:
            return page.url


class PageBlock(blocks.StructBlock):
    """Title and text nothing else"""
    title = blocks.CharBlock(required=True, help_text='page head title')
    content = blocks.TextBlock(required=True, help_text="page description")

    class Meta:
        template = "home/tittle_and_text_block.html"
        icon = "edit"
        label = "Title & Text"
        value_class = LinkStructValue


class UserBlock(blocks.StructBlock):
    """User Information Block"""
    first_name = blocks.CharBlock(required=True, help_text='first name')
    user_email = blocks.CharBlock(required=True, help_text='user email')
    surname = blocks.TextBlock(required=True, help_text="Add your bio")
    photo = ImageChooserBlock()
    role = blocks.CharBlock(required=True, help_text='User Role')

    class Meta:
        template = "home/tittle_and_text_block.html"
        icon = "user"
        label = "information about a user"
