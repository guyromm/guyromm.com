from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1248970646.0758591
_template_filename=u'/var/www/pylonsenv/guyromm/guyromm/templates/content/base-he.html'
_template_uri=u'/content/base-he.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['extra_css', 'sidebar_heading', 'sidebar_bottom', 'current_location_lbl', 'footer_txt']


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
    return runtime._inherit_from(context, 'base.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 10
        __M_writer(u'\n')
        # SOURCE LINE 17
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_css(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u"\n<style type='text/css'>\nbody {\ndirection:rtl;\n}\n</style>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sidebar_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\u05d0\u05ea\u05e8 \u05d4\u05d1\u05d9\u05ea \u05e9\u05dc \u05d2\u05d9\u05d0 \u05e8\u05d5\u05dd')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sidebar_bottom(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n<ul>\n<li><a href="http://photos.guyromm.com/">\u05ea\u05de\u05d5\u05e0\u05d5\u05ea</a></li>\n<li><a href="http://blog.guyromm.com/">\u05d1\u05dc\u05d5\u05d2</a></li>\n</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_current_location_lbl(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\u05de\u05d9\u05e7\u05d5\u05dd \u05e0\u05d5\u05db\u05d7\u05d9')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer_txt(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'&copy; 2008 \u05d2\u05d9\u05d0 \u05e8\u05d5\u05dd')
        return ''
    finally:
        context.caller_stack._pop_frame()


