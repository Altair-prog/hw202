from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='add_media_prefix')
def add_media_prefix(path):
    if path:
        return f'{settings.MEDIA_URL}{path}'
    return '#'
