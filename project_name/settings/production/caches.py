########## CACHE CONFIGURATION
CACHES['default']['BACKEND'] = 'django.core.cache.backends.memcached.MemcachedCache'
CACHES['default']['LOCATION'] = 'unix:%smemcached.sock' %
                                    normpath(join(DJANGO_ROOT, 'memcached/'))
########## END CACHE CONFIGURATION
