import os, sys
#sys.path.append('/usr/local/pylons/mysite')
os.environ['PYTHON_EGG_CACHE'] = '/tmp' 
#'/var/www/pylonsenv/lib/python2.5/site-packages/'



import site
site.addsitedir('/var/www/pylonsenv/lib/python2.6/site-packages')

from paste.deploy import loadapp
application = loadapp('config:/var/www/pylonsenv/guyromm/development.ini')
