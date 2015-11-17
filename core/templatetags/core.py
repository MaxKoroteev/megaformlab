# -*- coding: utf-8 -*-

from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, url_name, *url_params):
    if url_params and reverse(url_name, args=url_params) == context['request'].path:
        return ' active'
    if not url_params and reverse(url_name) == context['request'].path:
        return ' active'
    return ''
