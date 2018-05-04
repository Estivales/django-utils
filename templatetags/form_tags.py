# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

register = template.Library()

@register.simple_tag
def add_field_attr(field, attr, value):
    if field and field.field and field.field.widget:
        field.field.widget.attrs.update({attr: value})
    return field