# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294820744.334743
_template_filename=u'/var/www/pylonsenv/guyromm/guyromm/templates/content/skills_and_experience-en.html'
_template_uri=u'/content/skills_and_experience-en.html'
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
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 17
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_content(context):
    context.caller_stack._push_frame()
    try:
        url = context.get('url', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n<h1>Skills and Experience</h1>\n<p>To put it simply, I can probably create any kind of website/application that you could realistically come up with.</p>\n<dl> <dt>Development tools, environments, Operating Systems, etc.</dt> <dd>\n<p>I have a through knowledge of the GNU/Linux OS, both as an Administrator and a Developer. This means that I can not only write software, but can also set up complete solutions from the ground up - setting up a server, securing it, networking it, any services such as Mail, Web, File sharing and so on.</p>\n<p>But what I really am good at doing is implementing websites of any kind. I have a high degree of expertise and long experience with PHP, MySQL, PostgreSQL, Apache, and an endless list of related libraries, protocols, environments and tools. I\'ve had previous experience with a variety of other languages such as C++ and Microsoft Visual Studio, and am currently making way in becoming proficient in the Django environment and the Python programming language.</p>\n</dd> <dt>Tasks</dt> <dd>\n\n<p>I have succesfully built solutions for diverse sets of problems that include:</p>\n<dl> <dt>Search Engine Optimization</dt> <dd>I have previously set up from scratch a massive, distributed operation for SEO that included automatic generation and upload of distributed content, its interrelation and translation, link exchange with other websites, automating HTTP client-side operations with other websites, spidering other websites and analyzing search engine results.</dd> <dt>Billing and Affiliate Marketing systems</dt> <dd>I have built several systems whose purpose it is to bill customers and 2nd-tier partners, account for their traffic, compute revenue, generate reports, send E-Mail notifictions and so on.</dd> <dt>Massive customer traffic (re-)direction</dt> <dd>I have implemented systems that redirect customer traffic on a massive scale (hundreds of hits per second), based on automatic decision making from multiple overlapping factors.</dd> <dt>Complete websites</dt> <dd>that provide services such as Poker, which involves everything from user registration, administration tools and report generation,to CMS,  billing and  integration with other websites and sources of information such as Geolocation databases.</dd> <dt>Client side software and customization</dt> <dd>I have thorough experience in the implementation of client side solutions that utilize technologies such as JavaScript, AJAX, CSS. These are generally aimed at easing tasks for the user and making a site appear more friendly.</dd> </dl>  </dd><dt>Languages</dt> <dd>I fluently speak, read and write English, Hebrew and Russian.</dd> </dl>\n\n<p>To be fair, I\'ll point out what I cannot do. It\'s Graphics. I can only very poorly design the visual aspects of websites, and would rather focus on what I do best - programming.</p>\n<p><a href="')
        # SOURCE LINE 16
        __M_writer(escape(url.current(content='looking_for')))
        __M_writer(u'">&gt;&gt;&gt; Read on to find out what kind of projects I am interested in</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'&nbsp;\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


