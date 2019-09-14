import logging
#import inspect
# from pprint import pprint

class LoggingMiddleware:

    logger = logging.getLogger('development')

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # self.logger.info("req. client=" + request.get_host() + ", method=" + request.method
        #     + ", path=" + request.path + ", encoding=" + request.encoding
        #     + ", cookie=" + str(request.COOKIES or NOne) + ", meta=" + str(request.META or None))
        self.logger.info("req. {0}, {1}, {2}, [{3}], [{4}], [{5}], [{6}]"
            .format(self.s(request.META['REMOTE_HOST'])
                , request.method
                , request.path
                , self.s(request.COOKIES)
                , self.s(request.META['HTTP_USER_AGENT'])
                , self.s(request.META['HTTP_ACCEPT_ENCODING'])
                , self.s(request.META['HTTP_ACCEPT_LANGUAGE'])
                )
            )

        #pprint(request)
        response = self.get_response(request)
        self.logger.info("res. {0}, [{1}]"
            .format(response.status_code, response.serialize_headers()
            )
        )
        #self.logger.info("res. " + str(inspect.getmembers(response)))
        #pprint(response)
        return response

    def s(self, s):
        try: 
            if s == None:
                return ''
            return str(s)
        except:
            self.logger.error(e)
            return '[ERROR]'
