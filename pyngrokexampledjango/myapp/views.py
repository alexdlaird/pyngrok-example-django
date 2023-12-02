from django.http import JsonResponse
from django.views.decorators.cache import never_cache


@never_cache
def healthcheck(request):
    return JsonResponse(
        {
            "server": {"healthy": True}
        },
        status=200
    )
