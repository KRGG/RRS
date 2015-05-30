import os
from urlparse import urlparse
from django.core.urlresolvers import resolve
from django.core.urlresolvers import reverse

class DjangoLibrary(object):
    
    def resolve_url(self, url):

        try:
            path = urlparse(url).path
            resolution = resolve(path)
        except:
            raise RuntimeError('"{}" cannot be resolved to a named URL'.format(url))
            
        return resolution.url_name
    
    def reverse_url(self, url_name, *args):
        return reverse(url_name, args=args)