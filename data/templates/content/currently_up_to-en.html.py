# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294988569.4303679
_template_filename=u'/var/www/pylonsenv/guyromm/guyromm/templates/content/currently_up_to-en.html'
_template_uri=u'/content/currently_up_to-en.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['main_content', 'main_menu']


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
    return runtime._inherit_from(context, u'index-en.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 9
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_content(context):
    context.caller_stack._push_frame()
    try:
        url = context.get('url', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n<h1>What I am currently up to</h1>\n<br />\n<p>After going through a five year career in the Online Gambling industry, I\'ve decided to quit, and as of June 2008, I\'ve been tour cycling through Europe, with the general direction being East.*</p>\n<p>While taking the time to enjoy my trip, I haven\'t put aside my skills and have taken my computer along. The trip is open ended, and the immediate professional goal is to start carrying out projects while on the go. In order to achieve this, I am wildly experimenting with my lifestyle, my two main challenges being connectivity and dependance on electricity..</p>\n<p><a href="')
        # SOURCE LINE 8
        __M_writer(escape(url.current(content='looking_for')))
        __M_writer(u'">&gt;&gt;&gt; Read on to find out what I am looking for</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context):
    context.caller_stack._push_frame()
    try:
        url = context.get('url', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<a href="')
        __M_writer(escape(url.current(content='previous_work')))
        __M_writer(u'">Previous Work</a>')
        return ''
    finally:
        context.caller_stack._pop_frame()


