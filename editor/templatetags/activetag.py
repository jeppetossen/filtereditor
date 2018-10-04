from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag
def add_active(request, name, by_path=False):
    if by_path:
        path = name
    else:
        path = reverse(name)

    if request.path == path:
        return 'active'

    return ''
