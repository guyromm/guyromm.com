# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294820739.272223
_template_filename=u'/var/www/pylonsenv/guyromm/guyromm/templates/content/index-he.html'
_template_uri=u'/content/index-he.html'
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
    return runtime._inherit_from(context, u'base-he.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'                                                                ')
        __M_writer(u'\n                                      ')
        # SOURCE LINE 2
        __M_writer(u'\n                                           ')
        # SOURCE LINE 3
        __M_writer(u'\n                                           ')
        # SOURCE LINE 4
        __M_writer(u'\n                                                                       ')
        # SOURCE LINE 9
        __M_writer(u'\n                                                                    ')
        # SOURCE LINE 42
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_content(context):
    context.caller_stack._push_frame()
    try:
        url = context.get('url', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer(u'\n         <!--content_start(name:main_content,type:markup)--><h2>\u05d1\u05e8\u05d5\u05db\u05d9\u05dd \u05d4\u05d1\u05d0\u05d9\u05dd \u05dc-GuyRomm.com!</h2>\n                                                                                                \n<p>\u05de\u05d8\u05e8\u05ea\u05d5 \u05e9\u05dc \u05d4\u05d0\u05ea\u05e8 \u05d4\u05d9\u05d0 \u05dc\u05e1\u05e4\u05e8 \u05dc\u05de\u05d1\u05e7\u05e8\u05d9\u05d5 \u05d0\u05d5\u05d3\u05d5\u05ea\u05d9\u05d9, \u05dc\u05e2\u05d3\u05db\u05df \u05d0\u05ea\u05db\u05dd \u05d1\u05de\u05e2\u05e9\u05d9\u05d9 \u05d1\u05d6\u05de\u05df \u05d4\u05d0\u05d7\u05e8\u05d5\u05df, \u05d5\u05dc\u05d4\u05e4\u05e8\u05d9\u05d7 \u05e8\u05e2\u05d9\u05d5\u05e0\u05d5\u05ea \u05dc\u05e9\u05d9\u05ea\u05d5\u05e3 \u05e4\u05e2\u05d5\u05dc\u05d4 \u05d0\u05e4\u05e9\u05e8\u05d9 \u05d1\u05d9\u05e0\u05d9\u05e0\u05d5 \u05d1\u05ea\u05d7\u05d5\u05dd \u05d4\u05de\u05e7\u05e6\u05d5\u05e2\u05d9.\n                                                                                            </p>\n                                                                                                \n                                                                                          <br />\n<a href="')
        # SOURCE LINE 17
        __M_writer(escape(url.current(content='about_me')))
        __M_writer(u'">&gt;&gt;&gt;  \u05dc\u05e1\u05d9\u05db\u05d5\u05dd \u05e7\u05e6\u05e8\u05e6\u05e8 \u05d4\u05e7\u05dc\u05d9\u05e7\u05d5 \u05db\u05d0\u05df</a>\n<p>\u05d3\u05d1\u05e8\u05d9\u05dd \u05e8\u05d0\u05d5\u05d9\u05dd \u05dc\u05e6\u05d9\u05d5\u05df \u05e9\u05e2\u05e9\u05d9\u05ea\u05d9:</p>\n\n<div class=\'item\'>\n<a href=\'http://www.greenie.co.il/\'><img src=\'/images/snapshots/greenie.png\' alt="\u05e1\u05e7\u05e8\u05d9\u05e0\u05e9\u05d5\u05d8 \u05d2\u05e8\u05d9\u05e0\u05d9" /></a>\n<div class=\'descr\'><a href=\'http://www.greenie.co.il/\'>\u05d2\u05e8\u05d9\u05e0\u05d9</a> \u05de\u05e2\u05d5\u05d3\u05d3 \u05e9\u05dc\u05d9\u05d7\u05d5\u05d9\u05d5\u05ea \u05d0\u05d5\u05e4\u05e0\u05d9\u05d9\u05dd \u05d1\u05d9\u05e9\u05e8\u05d0\u05dc</div></div>\n \n <div class=\'item\'>\n <a href=\'http://www.bastarbut.com/\'><img src=\'/images/snapshots/bastarbut.png\' alt="\u05e1\u05e7\u05e8\u05d9\u05e0\u05e9\u05d5\u05d8 \u05d1\u05e1\u05d8\u05e8\u05d1\u05d5\u05ea" /></a>\n <div class=\'descr\'><a href=\'http://www.bastarbut.com/\'>\u05d1\u05e1\u05d8\u05e8\u05d1\u05d5\u05ea</a> \u05d4\u05d9\u05e0\u05d4 \u05d7\u05e0\u05d5\u05ea \u05de\u05e7\u05d5\u05d5\u05e0\u05ea \u05dc\u05de\u05d5\u05e6\u05e8\u05d9 \u05ea\u05e8\u05d1\u05d5\u05ea \u05e4\u05e8\u05d9\u05e0\u05d2\' \u05db\u05d2\u05d5\u05df \u05e1\u05e4\u05e8\u05d9\u05dd \u05d5\u05e1\u05e4\u05e8\u05d9 \u05e7\u05d5\u05de\u05d9\u05e7\u05e1.</div></div>\n\n <div class=\'item\'>\n <a href=\'/images/route.png\'><img src=\'/images/snapshots/biketrip.png\' alt="\u05e1\u05e7\u05e8\u05d9\u05e0\u05e9\u05d5\u05d8 \u05de\u05e1\u05dc\u05d5\u05dc \u05d8\u05d9\u05d5\u05dc \u05d0\u05d5\u05e4\u05e0\u05d9\u05d9\u05dd" /></a>\n <div class=\'descr\'>\u05d4\u05e2\u05d1\u05e8\u05ea\u05d9 \u05d0\u05ea \u05e7\u05d9\u05e5 2008 \u05d1\u05dc\u05d7\u05e6\u05d5\u05ea \u05d0\u05ea \u05d0\u05d9\u05e8\u05d5\u05e4\u05d4 \u05e2\u05dc \u05d0\u05d5\u05e4\u05e0\u05d9\u05d9\u05dd.</div></div>\n\n <div class=\'item\'>\n <a href=\'http://www.tet.co.il/\'><img src=\'/images/snapshots/tet.png\' alt="\u05e1\u05e7\u05e8\u05d9\u05e0\u05e9\u05d5\u05d8 \u05dc\u05d5\u05d7 \u05d8" /></a>\n <div class=\'descr\'><a href=\'http://www.tet.co.il/\'>\u05dc\u05d5\u05d7 \u05d8\'</a> \u05d4\u05d9\u05e0\u05d5 \u05dc\u05d5\u05d7 \u05de\u05d5\u05d3\u05e2\u05d5\u05ea \u05d7\u05d9\u05e0\u05de\u05d9, \u05de\u05e8\u05d5\u05d1\u05d4 \u05e9\u05e4\u05d5\u05ea \u05d5\u05d1\u05e2\u05dc \u05d0\u05d9\u05e0\u05d8\u05d2\u05e8\u05e6\u05d9\u05d4 \u05dc\u05e4\u05d9\u05d9\u05e1\u05d1\u05d5\u05e7 \u05d4\u05de\u05d1\u05d5\u05e1\u05e1 \u05e2\u05dc \u05d4\u05de\u05e8\u05d0\u05d4 \u05e9\u05dc \n</a> \u05e7\u05e8\u05d9\u05d9\u05d2\u05e1\u05dc\u05d9\u05e1\u05d8<a href=\'http://www.craigslist.org\'/>\n .</div></div>\n \n \n </p><!--content_end(name:main_conten t)-->\n\n\n                                                                                         ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context):
    context.caller_stack._push_frame()
    try:
        url = context.get('url', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n              <a href="')
        # SOURCE LINE 6
        __M_writer(escape(url.current(content='about_me')))
        __M_writer(u'">\u05d0\u05d5\u05d3\u05d5\u05ea\u05d9\u05d9</a> &nbsp; &nbsp; &nbsp; &nbsp;\n<a href="')
        # SOURCE LINE 7
        __M_writer(escape(url.current(content='skills_and_experience')))
        __M_writer(u'">\u05db\u05d9\u05e9\u05d5\u05e8\u05d9\u05dd \u05d5\u05e0\u05e1\u05d9\u05d5\u05df</a> &nbsp; &nbsp; &nbsp; &nbsp;\n             <a href="')
        # SOURCE LINE 8
        __M_writer(escape(url.current(content='contact')))
        __M_writer(u'">\u05d9\u05e6\u05d9\u05e8\u05ea \u05e7\u05e9\u05e8</a> &nbsp; &nbsp; &nbsp; &nbsp;\n                                                                                         ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_current_location(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\u05ea\u05dc-\u05d0\u05d1\u05d9\u05d1, \u05d9\u05e9\u05e8\u05d0\u05dc')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_header(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\u05e4\u05d9\u05ea\u05d5\u05d7 \u05d0\u05ea\u05e8\u05d9\u05dd \u05e2\u05dd \u05d7\u05d9\u05d5\u05da')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\u05d2\u05d9\u05d0 \u05e8\u05d5\u05dd - \u05e4\u05d9\u05ea\u05d5\u05d7 \u05d0\u05ea\u05e8\u05d9\u05dd \u05e2\u05dd \u05d7\u05d9\u05d5\u05da!')
        return ''
    finally:
        context.caller_stack._pop_frame()


