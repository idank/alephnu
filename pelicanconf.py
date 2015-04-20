#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Idan Kamara'
SITENAME = u'aleph.nu'
SITEURL = 'http://127.0.0.1:8000'

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

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
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

GITHUB_URL = "https://github.com/user/idank"

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# THEME = 'notmyidea'
THEME = '/Users/idank/dev/pelican-themes/nikhil-theme'

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['render_math']

ARTICLE_URL = 'blog/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORIES_URL = 'categories/{slug}/'
CATEGORIES_SAVE_AS = 'categories/{slug}/index.html'
AUTHOR_SAVE_AS = ''

STATIC_PATHS = ['images', 'css']
EXTRA_PATH_METADATA = {}

# put these files in the root of the output
for rootfile in ('CNAME', 'favicon.png', 'fsm.py', 'even-fsm.py'):
    STATIC_PATHS.append(rootfile)
    EXTRA_PATH_METADATA[rootfile] = {'path': rootfile}
