
class HostMiddleware(object):

    def process_request(self, request):
        print 'host = request.META', request.META.get('HTTP_HOST'), request.META.get('HTTP_X_FORWARDED_HOST')
        try:
            print 'host', request.get_host()
        except Exception, e:
            print 'e', e