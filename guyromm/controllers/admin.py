import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect as redirect_to

from guyromm.lib.base import BaseController, render
#from guyromm import model

log = logging.getLogger(__name__)

class AdminController(BaseController):
    def getessentials(self):
        from pylons import config
        import os,glob,re
        fre = re.compile('^(.*)\-([a-z]+)\.html$')
        c.allcontents=[]
        c.alllangs=[]
        c.contentsdict={}
        c.defnames=[]
        for infile in glob.glob(os.path.join(config['pylons.paths']['templates'][0],'content','*.html')):
            match = fre.match(os.path.split(infile)[-1])
            if match:
                shortname = match.group(1)
                lang = match.group(2)
                if lang not in c.alllangs: c.alllangs.append(lang)
                if shortname not in c.allcontents: c.allcontents.append(shortname)
                c.contentsdict['%s-%s'%(lang,shortname)]=infile
                #get the contents
                defre = re.compile(re.escape('<%def name=')+'(\'|")([^\'"]*)(\'|")>(.*)'+re.escape('</%def>'))
                fc = open(infile)
                defmatch = defre.findall(fc.read())
                if defmatch:
                    #log.debug('got matches in %s'%infile)
                    for onematch in defmatch:
                        if onematch[1] not in c.defnames: c.defnames.append(onematch[1])
            else:
                pass
                #log.debug('no match for %s'%infile)
    def index(self):
        self.getessentials()
        return render('/admin.html')
    def edit(self,lang,content):
        return render('/admin_form.html')
