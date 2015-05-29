import os
from urlparse import urlparse
from django.core.urlresolvers import resolve

class DjangoLibrary(object):
    
    def resolve_url(self, url):

        try:
            path = urlparse(url).path
            resolution = resolve(path)
        except:
            raise RuntimeError('"{}" cannot be resolved to a named URL'.format(url))
            
        return resolution.url_name