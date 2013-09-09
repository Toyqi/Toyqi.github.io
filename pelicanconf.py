#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Toyqi'
SITENAME = u'Toyqi的程序世界'
SITEURL = 'http://toyqi.github.io'

GITHUB_URL = 'https://github.com/toyqi'
ARCHIVES_URL = 'archives.html'
ARTICLE_URL = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

RELATIVE_URLS = True
DEFAULT_PAGINATION = 5

TIMEZONE = 'Asia/Shanghai'

THEME = 'tuxlite_tbs'

DEFAULT_LANG = u'zh'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

GOOGLE_ANALYTICS = 'UA-43842699-1'

GOOGLE_CUSTOM_SEARCH_SIDEBAR = '010598779893653790358:vf_znd6gjts'

DISQUS_SITENAME = 'wqiak47'

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

PLUGIN_PATH = u"pelican-plugins"
PLUGINS = ["sitemap"]
    
## 配置sitemap 插件
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

# Social widget
SOCIAL = (('Github', 'https://github.com/toyqi'),
          (u'微博', 'http://weibo.com/wqibyr'),
          (u'豆瓣', 'http://www.douban.com/people/Toyqi/'),
         )

# Blogroll
LINKS = (('Google', 'https://www.google.com/ncr'),
          ('Python', 'http://python.org/'),
          ('Pelican', 'http://docs.getpelican.com/'),
         )
