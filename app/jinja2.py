from __future__ import absolute_import  # Python 2 only

from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser
from jinja2 import Environment

def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': jinja_url,
        'user': AnonymousUser()
    })
    return env

def jinja_url(url, *args):
	return reverse(url, args=args)
