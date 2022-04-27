from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def current_page_title(page_name=''):
    return settings.APP_NAME + page_name
