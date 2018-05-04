# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

register = template.Library()

@register.filter
def percentage(fraction, population):
    return 100 * float(fraction)/float(population)

@register.filter
def subtract(value, arg):
    return int(value) - int(arg)

@register.filter
def divide(value, arg):
    return float(value) / float(arg)