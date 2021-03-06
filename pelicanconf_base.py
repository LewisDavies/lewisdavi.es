#!/usr/bin/env python
# -*- coding: utf-8 -*- #

##########
#
# Do not edit pelicanconf.py directly!
# Edit pelicanconf_base.py and the changes will propagate when
# the updated site is regenerated.
#
##########

from __future__ import unicode_literals
from datetime import date

AUTHOR = 'Lewis Davies'
SITENAME = 'DataNot.es'
SITEURL = 'http://datenot.es'
THEME = 'theme'
CURRENT_YEAR = date.today().year

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Full Stack Python', 'https://www.fullstackpython.com/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']

PLUGINS = ['render_math', 'sitemap', 'tipue_search']

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

EXTRA_PATH_METADATA = {
    'extra/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extra/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/site.webmanifest': {'path': 'site.webmanifest'}
}
