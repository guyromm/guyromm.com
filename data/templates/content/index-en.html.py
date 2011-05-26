# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294820629.14834
_template_filename=u'/var/www/pylonsenv/guyromm/guyromm/templates/content/index-en.html'
_template_uri=u'/content/index-en.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['main_content', 'main_menu', 'current_location', 'main_header', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        import guyromm.lib.helpers as h 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['h'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(u'\n')
        # SOURCE LINE 33
        __M_writer(u'\n')
        # SOURCE LINE 38
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_content(context):
    context.caller_stack._push_frame()
    try:
        url = context.get('url', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'\n<!--content_start(name:main_content,type:markup)--><h2>Welcome to GuyRomm.com!</h2>\n\n<p>The aim of this website is to introduce its visitors to who I am, what I am up to, and how I could potentially assist you with your ideas and business endeavours .<br />\n<br />\n<a href="')
        # SOURCE LINE 11
        __M_writer(escape(url.current(content='about_me')))
        __M_writer(u'">&gt;&gt;&gt; Read on for a brief summary</a></p><!--content_end(name:main_content)-->\n\n<p>Here are quick pointers to things I\'ve done:</p>\n\n<div class=\'item\'>\n<a href=\'http://www.greenie.co.il/en/\'><img src=\'/images/snapshots/greenie.png\' alt="greenie screenshot" /></a>\n<div class=\'descr\'><a href=\'http://www.greenie.co.il/en/\'>Greenie.co.il</a> tries to encourage bicycle deliveries in Israel</div></div>\n \n <div class=\'item\'>\n <a href=\'http://www.bastarbut.com/\'><img src=\'/images/snapshots/bastarbut.png\' alt="bastarbut screenshot" /></a>\n <div class=\'descr\'><a href=\'http://www.bastarbut.com/\'>Bastarbut.com</a> is an online shop for fringe culture creations, literature and comic books.</div></div>\n\n <div class=\'item\'>\n <a href=\'/images/route.png\'><img src=\'/images/snapshots/biketrip.png\' alt="biketrip route screenshot" /></a>\n <div class=\'descr\'>I\'ve spent the summer of 2008 crossing Europe on my bicycle.</div></div>\n\n <div class=\'item\'>\n <a href=\'http://www.tet.co.il/en/\'><img src=\'/images/snapshots/tet.png\' alt="tet screenshot" /></a>\n <div class=\'descr\'><a href=\'http://www.tet.co.il/en/\'>Tet.co.il</a> is a free, multilingual, facebook-enabled Israeli classifieds board in the spirit of Craigslist.</div></div>\n \n \n \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context):
    context.caller_stack._push_frame()
    try:
        url = context.get('url', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\n<a href="')
        # SOURCE LINE 35
        __M_writer(escape(url.current(content='about_me')))
        __M_writer(u'">About me</a> &nbsp; &nbsp; &nbsp; &nbsp;  \n<a href="')
        # SOURCE LINE 36
        __M_writer(escape(url.current(content='skills_and_experience')))
        __M_writer(u'">Skills &amp; Experience</a> &nbsp; &nbsp; &nbsp; &nbsp;  \n<a href="')
        # SOURCE LINE 37
        __M_writer(escape(url.current(content='contact')))
        __M_writer(u'">Contact</a> &nbsp; &nbsp; &nbsp; &nbsp;\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_current_location(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'Tel-Aviv, Israel')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_header(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'Web Development with a Smile')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Guy Romm - Web Development with a Smile!')
        return ''
    finally:
        context.caller_stack._pop_frame()


