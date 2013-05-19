"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from pylons import config
from routes import Mapper

def make_map():
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False
    
    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE
    #map.connect('/',controller='index',action='index',lang='en')
    #map.connect('/:lang/',controller='index',action='index')
    #map.connect('/:lang/:controller/',action='index')
    map.connect('/v2',controller='content',action='v2')
    map.connect('/',controller='content',action='serve',content='index',lang='en')
    map.connect('/{lang:(he|en)}/',controller='content',action='serve',content='index')
    map.connect('/{content}/',controller='content',action='serve',lang='en')
    map.connect('/{lang:(he|en)}/{content}/',controller='content',action='serve')

    map.connect('/{controller:admin}/{action:edit}/{content}/{lang}/')
    
    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')

    
    return map
