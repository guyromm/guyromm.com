from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1248985068.7488861
_template_filename=u'/var/www/pylonsenv/guyromm/guyromm/templates/content/contact-he.html'
_template_uri=u'/content/contact-he.html'
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
    return runtime._inherit_from(context, 'index-he.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_content(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n<h1>\u05d9\u05e6\u05d9\u05e8\u05ea \u05e7\u05e9\u05e8</h1>\n<p>\u05ea\u05e8\u05d2\u05d9\u05e9\u05d5 \u05d7\u05d5\u05e4\u05e9\u05d9\u05d9\u05dd \u05dc\u05db\u05ea\u05d5\u05d1 \u05d0\u05dc\u05d9 \u05d1<a href="mailto:guyromm@gmail.com">guyromm@gmail.com</a>.\n\n<p>\n\u05d1\u05d4\u05d9\u05d5\u05d5\u05e6\u05e8 \u05d4\u05e6\u05d5\u05e8\u05da, \u05e0\u05d9\u05ea\u05df \u05d9\u05d4\u05d9\u05d4 \u05dc\u05e2\u05d1\u05d5\u05e8 \u05dc\u05d0\u05d5\u05e4\u05df \u05d4\u05ea\u05e7\u05e9\u05e8\u05d5\u05ea \u05d9\u05e9\u05d9\u05e8 \u05d9\u05d5\u05ea\u05e8.\n</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


