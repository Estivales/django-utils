# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.utils import timezone
from django.utils.dateparse import parse_datetime as convert_datetime, parse_date as convert_date
register = template.Library()

@register.filter
def parse_datetime(value):
    if not value:
        return None
    return convert_datetime(value)

@register.filter
def parse_date(value):
    if not value:
        return None
    return convert_date(value)


@register.filter
def date_in_future(datahora):
    if isinstance(datahora, datetime.datetime):
        return datahora and datahora > timezone.now()
    elif isinstance(datahora, datetime.date):
        return datahora and datahora > timezone.now().date()
    return None