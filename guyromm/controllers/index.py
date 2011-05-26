import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect as redirect_to

from guyromm.lib.base import BaseController, render
#from guyromm import model

log = logging.getLogger(__name__)

class IndexController(BaseController):
    def index(self,lang):
        return render('/index-%s.html'%lang)
