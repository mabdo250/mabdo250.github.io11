#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

#########################################################################################
#

TIMEZONE = 'Africa/Cairo'
DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8'

#########################################################################################
# METADATA

AUTHOR = 'Mohamed Abdo'
SITENAME = 'Mohamed Abdo'
SITESUBTITLE = '&#x1F52C; Data Analyst | &#128104;&#8205;&#9877;&#65039; Medical Student '

#########################################################################################
# PATHS

SITEURL = ''
PATH = 'content'
FAVICON = 'favicon.ico'
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_PATHS = ['images', 'static', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'}}

#ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
#ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'


ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#########################################################################################
# FEEDS

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#########################################################################################
# LINKS

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/msalah_abdo'),
          ('github', 'https://github.com/mabdo250e'),
          ('facebook','https://www.facebook.com/msalah250'),
          ('linkedin', 'https://www.linkedin.com/in/msalah-abdo/'),)

#########################################################################################
# CONTENT

DEFAULT_PAGINATION = False
DELETE_OUTPUT_DIRECTORY = True
TYPOGRIFY = True

#########################################################################################
# THEME

THEME_PATH = os.path.join(BASE_PATH, 'themes')
THEME = os.path.join(THEME_PATH, 'pelican-clean-blog-master')
DISPLAY_PAGES_ON_MENU = True
HEADER_COVER = 'images/main_header/data3.jpg'
CSS_OVERRIDE = 'static/css/custom.css'

COLOR_SCHEME_CSS = 'github.css'

#########################################################################################
# PLUGINS

PLUGIN_BASE = os.path.join(BASE_PATH, 'plugins')
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = [PLUGIN_BASE]
PLUGINS = ['pelican-ipynb-master.markup','sub_parts']
IPYNB_USE_META_SUMMARY = True
IGNORE_FILES = ['.ipynb_checkpoints']
IPYNB_IGNORE_CSS = True
