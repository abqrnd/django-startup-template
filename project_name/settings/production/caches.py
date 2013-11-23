from os.path import normpath, join
from . import DJANGO_ROOT
from . import CACHES

CACHES['default']['BACKEND'] = 'django.core.cache.backends.memcached.MemcachedCache'
CACHES['default']['LOCATION'] = 'unix:%smemcached.sock' % \
                                    normpath(join(DJANGO_ROOT, 'memcached/'))
