# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.template.defaultfilters import stringfilter
import re
register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def remove_tags(value, tags):
    tags = [re.escape(tag) for tag in tags.split()]
    tags_re = '(%s)' % '|'.join(tags)
    starttag_re = re.compile(r'<%s(/?>|(\s+[^>]*>))' % tags_re, re.U)
    endtag_re = re.compile('</%s>' % tags_re)
    value = starttag_re.sub('', value)
    value = endtag_re.sub('', value)
    return value
