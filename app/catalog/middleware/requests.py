from ..services import CachingService


class LogUsersRequestsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        service = CachingService(request, response)
        if not service.add_to_cache():
            print("Couldn't log user's request")

        return response

