from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1250486563.568568
_template_filename=u'/var/www/pylonsenv/guyromm/guyromm/templates/content/previous_work-he.html'
_template_uri=u'/content/previous_work-he.html'
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
        # SOURCE LINE 14
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_content(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n<h1>\u05e2\u05d1\u05d5\u05d3\u05d5\u05ea \u05e7\u05d5\u05d3\u05de\u05d5\u05ea</h1>\n<dt><a href="http://www.tet.co.il/">www.tet.co.il</a></dt> <dd>\u05dc\u05d5\u05d7 \u05de\u05d5\u05d3\u05e2\u05d5\u05ea \u05d7\u05d9\u05e0\u05de\u05d9 \u05d4\u05ea\u05d5\u05de\u05da \u05d1\u05e8\u05d9\u05d1\u05d5\u05d9 \u05e9\u05e4\u05d5\u05ea, \u05d0\u05d9\u05e0\u05d8\u05d2\u05e8\u05e6\u05d9\u05d4 \u05e2\u05dd \u05e4\u05d9\u05d9\u05e1\u05d1\u05d5\u05e7 \u05d5\u05d1\u05e2\u05dc \u05d5\u05de\u05d2\u05d5\u05d5\u05df \u05ea\u05db\u05d5\u05e0\u05d5\u05ea \u05de\u05ea\u05e7\u05d3\u05de\u05d5\u05ea \u05d0\u05d7\u05e8\u05d5\u05ea.</dd>  \n\n<dt><a href="http://www.redkings.com/">www.redkings.com</a></dt> <dd>\u05d0\u05ea\u05e8 \u05e4\u05d5\u05e7\u05e8 \u05d4\u05de\u05d1\u05d5\u05e1\u05e1 \u05e2\u05dc \u05e4\u05dc\u05d8\u05e4\u05d5\u05e8\u05de\u05ea ONGame.</dd> \n\n<dt><a href="http://www.bastarbut.com/">www.bastarbut.com</a></dt> <dd>\u05d7\u05e0\u05d5\u05ea \u05e1\u05e4\u05e8\u05d9\u05dd \u05de\u05e7\u05d5\u05d5\u05e0\u05ea \u05d4\u05de\u05ea\u05de\u05d7\u05d4 \u05d1\u05ea\u05d7\u05d5\u05dd \u05d4\u05d0\u05d9\u05e0\u05d3\u05d9 \u05d5\u05ea\u05e8\u05d1\u05d5\u05ea \u05d4\u05e4\u05e8\u05d9\u05e0\u05d2\'</dd></dd>\n\n</dl>\n<p>\u05e7\u05d9\u05e9\u05d5\u05e8\u05d9\u05dd \u05d0\u05dc\u05d5 \u05d4\u05dd \u05d8\u05e2\u05d9\u05de\u05d4. \u05de\u05e1\u05d9\u05d1\u05d5\u05ea \u05e9\u05d5\u05e0\u05d5\u05ea \u05d0\u05e0\u05d9 \u05de\u05e0\u05d5\u05e2 \u05de\u05dc\u05e4\u05e8\u05e1\u05dd \u05e2\u05d1\u05d5\u05d3\u05d5\u05ea \u05d0\u05d7\u05e8\u05d5\u05ea.</p>\n')
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


