# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294820743.3259671
_template_filename=u'/var/www/pylonsenv/guyromm/guyromm/templates/content/about_me-en.html'
_template_uri=u'/content/about_me-en.html'
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
        # SOURCE LINE 15
        __M_writer(u'\n')
        # SOURCE LINE 19
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_content(context):
    context.caller_stack._push_frame()
    try:
        url = context.get('url', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u"\n<h1>About me</h1>\n<br />\nHello, my name is Guy Romm. Being an Israeli of Russian-Jewish origin presented me with a duality of perspectives early on as I grew up. At that, growing up in Israel, I&#x27;ve never completely assimilated with local culture, and that caused and still is causing me to push the envelope in search of the place and form to be. Doesn't make much sense? No worries, I'm still trying to figure that one out myself..<br />\n<br />\n\nFrom a young age, I have been interested in Computers and Information Technology, and at the age of ")
        # SOURCE LINE 8
        __M_writer(escape(c.myage))
        __M_writer(u', I can confidently say that I\'ve acquired a wide and thorough expertise in a series of professional fields, the presentation of which is the purpose of this website.<br />\n<br />\nYou are welcome to read the following pages of this site to see if there is grounds for a possible collaboration between us.<br />\n\n<br />\n<a href="')
        # SOURCE LINE 13
        __M_writer(escape(url.current(content='skills_and_experience')))
        __M_writer(u'">&gt;&gt;&gt; Read an overview of my professional experience</a><br />\n<a href="')
        # SOURCE LINE 14
        __M_writer(escape(url.current(content='currently_up_to')))
        __M_writer(u'">&gt;&gt;&gt; Find out what I am currently doing</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context):
    context.caller_stack._push_frame()
    try:
        url = context.get('url', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 16
        __M_writer(u'\n<a href="')
        # SOURCE LINE 17
        __M_writer(escape(url.current(content='currently_up_to')))
        __M_writer(u'">Currently up to</a> &nbsp; &nbsp; &nbsp; &nbsp;   \n<a href="')
        # SOURCE LINE 18
        __M_writer(escape(url.current(content='looking_for')))
        __M_writer(u'">What I am looking for</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


