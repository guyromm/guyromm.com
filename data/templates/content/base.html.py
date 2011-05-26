# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294820615.209424
_template_filename=u'/var/www/pylonsenv/guyromm/guyromm/templates/content/base.html'
_template_uri=u'/content/base.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['sidebar', 'current_location_lbl', 'text_div_params', 'sidebar_heading', 'sidebar_bottom', 'footer_txt', 'extra_css']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<!--\nAuthor: Reality Software\nWebsite: http://www.realitysoftware.ca\nNote: This is a free template released under the Creative Commons Attribution 3.0 license, \nwhich means you can use it in any way you want provided you keep the link to the author intact.\n-->\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n<title>')
        # SOURCE LINE 11
        __M_writer(escape(self.title()))
        __M_writer(u'</title><!--content_end(name:title)-->\n<link rel="stylesheet" type="text/css" href="/style.css"/>\n</head>\n')
        # SOURCE LINE 14
        __M_writer(u'\n')
        # SOURCE LINE 15
        __M_writer(escape(self.extra_css()))
        __M_writer(u'\n<body>\n\n<div id="container">\n\n<div id="header">\n<a href="')
        # SOURCE LINE 21
        __M_writer(escape(url.current(content='index')))
        __M_writer(u'">')
        __M_writer(escape(self.main_header()))
        __M_writer(u'</a>\n\n</div>\n\n<div id="menu">\n\n\n')
        # SOURCE LINE 28
        __M_writer(escape(self.main_menu()))
        __M_writer(u'\n\n<!--content_start(name:main_menu,type:markup)--><!--content_end(name:main_menu)-->\n\n</div>\n')
        # SOURCE LINE 33
        __M_writer(u'\n')
        # SOURCE LINE 34
        __M_writer(u'\n')
        # SOURCE LINE 58
        __M_writer(u'\n')
        # SOURCE LINE 83
        __M_writer(u'\n')
        # SOURCE LINE 85
        __M_writer(escape(self.sidebar()))
        __M_writer(u'\n\n<div id="main">\n')
        # SOURCE LINE 88
        __M_writer(u'\n<div id="text" ')
        # SOURCE LINE 89
        __M_writer(escape(self.text_div_params()))
        __M_writer(u'>\n')
        # SOURCE LINE 90
        __M_writer(escape(self.main_content()))
        __M_writer(u'\n</div>\n\n<div class="clear"></div>\n\n</div>\n\n<div id="footer">\n')
        # SOURCE LINE 100
        __M_writer(u'\n')
        # SOURCE LINE 101
        __M_writer(escape(self.footer_txt()))
        __M_writer(u' &nbsp;<span class="separator">|</span> &nbsp; \n\n<!-- DO NOT DELETE THIS LINK! READ THE LICENSE! -->\nDesign by <a href="http://www.realitysoftware.ca" title="Website Design">Reality Software</a>\n<!-- ****************************************** -->\n</div>\n\n</div>\n<script type="text/javascript">\nvar gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");\ndocument.write(unescape("%3Cscript src=\'" + gaJsHost + "google-analytics.com/ga.js\' type=\'text/javascript\'%3E%3C/script%3E"));\n</script>\n<script type="text/javascript">\nvar pageTracker = _gat._getTracker("UA-135121-2");\npageTracker._initData();\npageTracker._trackPageview();\n</script>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sidebar(context):
    context.caller_stack._push_frame()
    try:
        url = context.get('url', UNDEFINED)
        self = context.get('self', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 59
        __M_writer(u'\n<div id="sidebar">\n\n<h1>')
        # SOURCE LINE 62
        __M_writer(escape(self.sidebar_heading()))
        __M_writer(u'</h1>\n\n\n<p>')
        # SOURCE LINE 65
        __M_writer(escape(self.current_location_lbl()))
        __M_writer(u': <b>')
        __M_writer(escape(self.current_location()))
        __M_writer(u'.</b></p>\n\n')
        # SOURCE LINE 67
        if c.langsavail:
            # SOURCE LINE 68
            __M_writer(u'<p>\n[\n')
            # SOURCE LINE 70
            for lang in c.langsavail:
                # SOURCE LINE 71
                __M_writer(u'<a href="')
                __M_writer(escape(url.current(lang=lang)))
                __M_writer(u'">')
                __M_writer(escape(c.lang_labels[lang]))
                __M_writer(u'</a>\n')
                # SOURCE LINE 72
                if lang != c.langsavail[-1]:
                    # SOURCE LINE 73
                    __M_writer(u'&nbsp;,&nbsp;\n')
                    pass
                pass
            # SOURCE LINE 76
            __M_writer(u']\n</p>\n')
            pass
        # SOURCE LINE 79
        __M_writer(u'<p>\n')
        # SOURCE LINE 80
        __M_writer(escape(self.sidebar_bottom()))
        __M_writer(u'\n</p>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_current_location_lbl(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'Current location')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_text_div_params(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sidebar_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 33
        __M_writer(u"Guy Romm's website")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sidebar_bottom(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 35
        __M_writer(u'\n<ul class=stream>\n<li><a href="http://photos.guyromm.com/">Photos</a></li>\n<li><a href="http://blog.guyromm.com/">Blog</a></li>\n</ul>\n\n')
        # SOURCE LINE 41
        if len(c.posts):
            # SOURCE LINE 42
            __M_writer(u'<h4>Facebook stream</h4>\n<small><a href="http://www.facebook.com/guyromm">link to profile</a></small><br />\n<ul class=stream>\n')
            # SOURCE LINE 45
            import re 
            
            __M_writer(u'\n')
            # SOURCE LINE 46
            for p in c.posts:
                # SOURCE LINE 47
                if len(p['message']): 
                    # SOURCE LINE 48
                    __M_writer(u'<li>')
                    __M_writer(re.compile('http\:\/\/([^ \/]*)([^ ]*)').sub('<a href="http://\\1\\2">\\1</a>',p['message'][:70]))
                    __M_writer(u'')
                    # SOURCE LINE 49
                    if len(p['message'])>70:
                        # SOURCE LINE 50
                        __M_writer(u'...\n')
                        pass
                    # SOURCE LINE 52
                    __M_writer(u'</li>\n')
                    pass
                # SOURCE LINE 54
                __M_writer(u'\n')
                pass
            # SOURCE LINE 56
            __M_writer(u'</ul>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer_txt(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 98
        __M_writer(u'\n&copy;2008 Guy Romm\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_css(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


