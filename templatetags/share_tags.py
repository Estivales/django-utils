# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urllib

from django.conf import settings
from django.template import Library
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext

register = Library()

@register.simple_tag
def current_site_url():
    protocol = getattr(settings, 'MY_SITE_PROTOCOL', 'https')
    port = getattr(settings, 'MY_SITE_PORT', '')
    url = '%s://%s' % (protocol, settings.SITE_DOMAIN)
    if port:
        url += ':%s' % port
    return url

@register.simple_tag
def tweet_it(request, url, title):
    return mark_safe("""
        <div class="twitter">
            <a href="http://twitter.com/home/?%s" title="%s" target="_blank"></a>
        </div>    
    """ % (urllib.urlencode({'status': title + (u" " + url + u" #escalibro").encode('utf-8')}), ugettext("Tweet it")))


@register.simple_tag
def tweet_like(request, url, title):
    return mark_safe("""
        <iframe allowtransparency="true" frameborder="0" scrolling="no" tabindex="0" class="twitter-share-button twitter-count-horizontal" 
                src="https://platform.twitter.com/widgets/tweet_button.html?_=1302382076454&amp;count=horizontal&amp;lang=en&amp;via=escalibro&amp;%s" 
                style="width: 110px; height: 20px; " title="Twitter For Websites: Tweet Button"></iframe>
        <script type="text/javascript" src="https://platform.twitter.com/widgets.js"></script>
    """ % ('text=' + title + ' %23escalibro&amp;' + urllib.urlencode({'url': url})))


@register.simple_tag
def facebook_it(request, url, title):
    return mark_safe("""
        <div class="facebook">
            <a onclick="window.open(this.href, '%s', 'width=800,height=300'); return false" href="https://www.facebook.com/sharer.php?%s" title="%s" target="_blank"></a>
        </div>
    """ % (ugettext("Share link on FaceBook"), urllib.urlencode({'u': url, 't': title}), ugettext("To FaceBook")))


@register.simple_tag
def facebook_like(request, url, title):
    return mark_safe("""
        <iframe src="https://www.facebook.com/plugins/like.php?href%s&amp;layout=button_count&amp;show_faces=true&amp;width=85&amp;action=like&amp;colorscheme=light&amp;height=21" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:85px; height:21px;" allowtransparency="true"></iframe>
    """ % (urllib.urlencode({'': url})))