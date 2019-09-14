import logging

class LoggingMiddleware:

    logger = logging.getLogger('development')

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.logger.info("LoggingMiddleware.req")
        response = self.get_response(request)
        self.logger.info("LoggingMiddleware.res")
        return response