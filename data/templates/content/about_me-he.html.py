# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1295065816.8104551
_template_filename=u'/var/www/pylonsenv/guyromm/guyromm/templates/content/about_me-he.html'
_template_uri=u'/content/about_me-he.html'
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
    return runtime._inherit_from(context, u'index-he.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(u'\n')
        # SOURCE LINE 24
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
        # SOURCE LINE 6
        __M_writer(u'\n<h2>\u05d0\u05d5\u05d3\u05d5\u05ea\u05d9\u05d9</h2>\n\n<p>\n \u05db\u05d4\u05e9\u05dc\u05db\u05d4 \u05de\u05db\u05da \u05e9\u05e0\u05d5\u05dc\u05d3\u05ea\u05d9 \u05d1\u05de\u05d7\u05d5\u05d6\u05d5\u05ea \u05d0\u05d7\u05e8\u05d9\u05dd (\u05d4\u05e2\u05d9\u05e8 \u05e7\u05d6\u05d0\u05df \u05e9\u05d1\u05e8\u05d5\u05e1\u05d9\u05d4), \u05e0\u05ea\u05d1\u05e8\u05db\u05ea\u05d9 \u05d1\u05d3\u05d5\u05d0\u05dc\u05d9\u05d5\u05ea \u05e9\u05dc \u05e4\u05e8\u05e1\u05e4\u05e7\u05d8\u05d9\u05d1\u05d5\u05ea \u05e2\u05dd \u05d4\u05ea\u05d1\u05d2\u05e8\u05d5\u05ea\u05d9 \u05d1\u05d0\u05e8\u05e5, \u05e9\u05ea\u05e8\u05de\u05d4 \u05dc\u05d4\u05d1\u05e0\u05ea\u05d9 \u05d0\u05ea \u05d4\u05de\u05e6\u05d9\u05d0\u05d5\u05ea \u05d4\u05dc\u05e2\u05d9\u05ea\u05d9\u05dd \u05d0\u05d1\u05e1\u05d5\u05e8\u05d3\u05d9\u05ea \u05e9\u05e1\u05d1\u05d9\u05d1\u05d9. <br />\n\u05d0\u05da \u05dc\u05db\u05dc \u05de\u05d8\u05d1\u05e2 \u05e9\u05e0\u05d9 \u05e6\u05d3\u05d3\u05d9\u05dd, \u05d5\u05de\u05d0\u05d5\u05ea\u05df \u05d4\u05e1\u05d9\u05d1\u05d5\u05ea \u05d2\u05dd \u05dc\u05d0 \u05d4\u05e8\u05d2\u05e9\u05ea\u05d9 \u05e9\u05d9\u05d9\u05da, \u05d5\u05de\u05e1\u05d9\u05d1\u05d4 \u05d6\u05d5 \u05d1\u05e2\u05d9\u05e7\u05e8 \u05d1\u05e9\u05e0\u05d9\u05dd \u05d4\u05d0\u05d7\u05e8\u05d5\u05e0\u05d5\u05ea \u05d0\u05e0\u05d9 \u05de\u05e0\u05d4\u05dc \u05de\u05e1\u05e2 \u05e4\u05e2\u05d9\u05dc \u05dc\u05de\u05e6\u05d9\u05d0\u05ea \u05d4\u05de\u05e7\u05d5\u05dd \u05d5\u05d4\u05e6\u05d5\u05e8\u05d4 \u05d1\u05d4\u05dd \u05e2\u05dc\u05d9 \u05dc\u05d4\u05d9\u05d5\u05ea. \u05dc\u05d0 \u05db"\u05db \u05d1\u05e8\u05d5\u05e8? \u05dc\u05d0 \u05e0\u05d5\u05e8\u05d0, \u05d2\u05dd \u05dc\u05d9 \u05e2\u05d3\u05d9\u05d9\u05df \u05dc\u05d0.. \n</p>\n\n<p>\u05de\u05d2\u05d9\u05dc \u05e6\u05e2\u05d9\u05e8, \u05d2\u05d9\u05dc\u05d9\u05ea\u05d9 \u05e2\u05e0\u05d9\u05d9\u05df \u05e8\u05d1 \u05d1\u05de\u05d7\u05e9\u05d1\u05d9\u05dd \u05d5\u05d8\u05db\u05e0\u05d5\u05dc\u05d5\u05d2\u05d9\u05d9\u05ea \u05de\u05d9\u05d3\u05e2 \u05d5\u05db\u05e2\u05ea, \u05d1\u05d2\u05d9\u05dc ')
        # SOURCE LINE 14
        __M_writer(escape(c.myage))
        __M_writer(u', \u05d9\u05db\u05d5\u05dc \u05d0\u05e0\u05d9 \u05dc\u05d4\u05d2\u05d9\u05d3 \u05d1\u05d1\u05d8\u05d7\u05d5\u05df \u05e9\u05e6\u05d1\u05e8\u05ea\u05d9 \u05e0\u05e1\u05d9\u05d5\u05df \u05e8\u05d1 \u05d5\u05d9\u05e1\u05d5\u05d3\u05d9 \u05d1\u05e1\u05d3\u05e8\u05ea \u05ea\u05d7\u05d5\u05de\u05d9\u05dd \u05de\u05e7\u05e6\u05d5\u05e2\u05d9\u05d9\u05dd, \u05e9\u05e1\u05e7\u05d9\u05e8\u05ea\u05dd \u05d4\u05d9\u05d0 \u05de\u05d8\u05e8\u05ea\u05d5 \u05d4\u05de\u05e8\u05db\u05d6\u05d9\u05ea \u05e9\u05dc \u05d0\u05ea\u05e8 \u05d6\u05d4.\n</p>\n\n<p>\u05d4\u05e0\u05db\u05dd \u05de\u05d5\u05d6\u05de\u05e0\u05d9\u05dd \u05dc\u05e7\u05e8\u05d5\u05d0 \u05d0\u05ea \u05d4\u05d3\u05e4\u05d9\u05dd \u05d4\u05d1\u05d0\u05d9\u05dd, \u05db\u05d3\u05d9 \u05dc\u05d4\u05ea\u05e8\u05e9\u05dd \u05d1\u05d0\u05dd \u05d9\u05e9 \u05e7\u05e8\u05e7\u05e2 \u05dc\u05e9\u05d9\u05ea\u05d5\u05e3 \u05e4\u05e2\u05d5\u05dc\u05d4 \u05d1\u05d9\u05e0\u05d9\u05e0\u05d5.\n</p>\n\n<p>\n<a href="')
        # SOURCE LINE 21
        __M_writer(escape(url.current(content='skills_and_experience')))
        __M_writer(u'">&gt;&gt;&gt;  \u05dc\u05e1\u05e7\u05d9\u05e8\u05d4 \u05e9\u05dc \u05e0\u05e1\u05d9\u05d5\u05e0\u05d9 \u05d4\u05de\u05e7\u05e6\u05d5\u05e2\u05d9</a><br />\r<a href="')
        __M_writer(escape(url.current(content='currently_up_to')))
        __M_writer(u'">&gt;&gt;&gt; \u05de\u05d4 \u05de\u05e2\u05e9\u05d9\u05d9 \u05db\u05e8\u05d2\u05e2</a>\r\n\n</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context):
    context.caller_stack._push_frame()
    try:
        url = context.get('url', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n<a href="')
        # SOURCE LINE 3
        __M_writer(escape(url.current(content='currently_up_to')))
        __M_writer(u'">\u05de\u05e2\u05e9\u05d9\u05d9 \u05db\u05e2\u05ea</a> &nbsp; &nbsp; &nbsp; &nbsp;   \n<a href="')
        # SOURCE LINE 4
        __M_writer(escape(url.current(content='looking_for')))
        __M_writer(u'">\u05de\u05d4 \u05d0\u05e0\u05d9 \u05de\u05d7\u05e4\u05e9</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


