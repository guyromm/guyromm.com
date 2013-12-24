# -*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect as redirect_to

from guyromm.lib.base import BaseController, render
#from guyromm import model

log = logging.getLogger(__name__)

class ContentController(BaseController):
    def serve(self,lang,content):
        if request.params.get('exc',False):
            raise Exception('testicle')

        if request.params.get('exc',False): raise Exception('whatevah1')
        import datetime
        c.myage = (datetime.datetime.now()-datetime.datetime(1982,8,14)).days/365
        c.posts=[]

        langs = ['he','en']
        if lang not in langs:
            raise Exception('unknown language %s'%lang)
        from pylons import config
        import os
        tpldir = config['pylons.paths']['templates'][0]
        pathpat = '%s/content/%s-%s.html'
        fnpat = '/content/%s-%s.html'
        casc = ({'fullfn':pathpat%(tpldir,content,lang),
                 'lang':lang,
                 'shortfn':fnpat%(content,lang)}
                ,{'fullfn':pathpat%(tpldir,content,'en'),
                  'lang':'en',
                  'shortfn':fnpat%(content,'en')})
        log.debug('lang is %s'%lang)
        c.lang_labels={'he':u'עברית','en':u'English'}
        c.langsavail=[]
        for tlang in langs:
            if os.path.exists(pathpat%(tpldir,content,tlang)):
                c.langsavail.append(tlang)

        for f in casc:
            if os.path.exists(f['fullfn']):
                log.debug('rendering %s'%f['shortfn'])
                c.curlang=f['lang']
                del c.langsavail[c.langsavail.index(c.curlang)]
                return render(f['shortfn'])
            else:
                log.debug('cannot find %s'%f['fullfn'])
        
        return abort(404,'404 not found')

        from guyromm.controllers.error import ErrorController
        request.environ['pylons.original_response']=object()
        setattr(request.environ['pylons.original_response'],'body','404 not found')
        ec =  ErrorController()
        return ec.document()
        #return cfn+str(os.path.exists(cfn))
        #return render('/%s-%s.html'%(content,lang))

