# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294820747.0399809
_template_filename=u'/var/www/pylonsenv/guyromm/guyromm/templates/content/looking_for-en.html'
_template_uri=u'/content/looking_for-en.html'
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
        # SOURCE LINE 14
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
        __M_writer(u'\n<h1>What kind of work I am looking for</h1>\n<br />\n<p>I quit working for the Gambling Industry after realizing that I can do so much more for my surrounding world than just creating ways for money to move from one pocket to another.</p>\n<p>Currently, I am looking for projects that can assist people, make their life easier, solve common tasks, simplify life or even just make it a tad more enjoyable.</p>\n<p>I will turn down projects whose sole purpose is making money in corruptive ways such as spam, SEO and other endevours of parasitical nature.</p>\n<p>However, marketing projects that solve a genuine problem, address or pin point a target audience more efficiently, save people a headache, etc. are welcome.</p>\n<p>I would also consider projects that don\'t explicitly or directly have a &quot;positive&quot; value, so long as they are not harmful, are interesting, and the remuneration is worthwhile..</p>\n\n<p>And if you think that you\'ve got a bright idea that I can implement, tell me about it. We can find a way to bring it into existance!</p>\n<p><a href="')
        # SOURCE LINE 13
        __M_writer(escape(url.current(content='contact')))
        __M_writer(u'">&gt;&gt;&gt; To contact me, click here</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'&nbsp;')
        return ''
    finally:
        context.caller_stack._pop_frame()


