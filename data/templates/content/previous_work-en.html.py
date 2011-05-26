from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1250526081.7214351
_template_filename=u'/var/www/pylonsenv/guyromm/guyromm/templates/content/previous_work-en.html'
_template_uri=u'/content/previous_work-en.html'
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
    return runtime._inherit_from(context, 'index-en.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 16
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_content(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n<h1>Previous work</h1>\n<br />\n<dl> \n\n<dt><a href="http://www.tet.co.il/">www.tet.co.il</a></dt> <dd>A free, uncommercial, multilingual classifieds website with Facebook integration and other unique qualities.</dd>  \n\n<dt><a href="http://www.redkings.com/">www.redkings.com</a></dt> <dd>A poker website based on the ONGame platform.</dd> \n\n<dt><a href="http://www.bastarbut.com/">www.bastarbut.com</a></dt> <dd>An online bookstore specializing in Indie titles and fringe culture.</dd></dd>\n\n</dl>\n<p>These are just a tasting, however. For various reasons I am restricted from openly showing other work.</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'&nbsp')
        return ''
    finally:
        context.caller_stack._pop_frame()


