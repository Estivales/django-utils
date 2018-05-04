# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from money.money import Money

register = template.Library()

@register.assignment_tag
def set(val=None):
    return val

@register.filter
def remove_substring(value, char):
    return value.replace(char,"")

@register.filter
def cents_to_brl(value):
    if value:
        value = int(value)
        # valor com centavos em float
        value = float(value) / 100
        m = Money(value, "BRL")
        return m.format("pt_BR", "¤ #,##0.00")
    return None