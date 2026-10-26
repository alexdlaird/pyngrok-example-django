__copyright__ = "Copyright (c) 2026 Alex Laird"
__license__ = "MIT"


class MuppetsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        response['X-Muppets'] = '42'

        return response
