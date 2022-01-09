from polls.models import Log


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    @staticmethod
    def process_view(request, view_func, view_args, view_kwargs):
        if not request.path.startswith('/admin/'):
            Log.objects.create(path=request.path, method=request.method)
