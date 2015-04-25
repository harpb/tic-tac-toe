from django.conf import settings

class HostMiddleware(object):

    def process_request(self, request):
        print 'host = request.META', request.META.get('HTTP_HOST'), request.META.get('HTTP_X_FORWARDED_HOST')
        print 'settings.ALLOWED_HOSTS', settings.ALLOWED_HOSTS
        try:
            print 'host', request.get_host()
        except Exception, e:
            print 'e', e