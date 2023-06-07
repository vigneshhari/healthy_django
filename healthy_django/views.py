from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from healthy_django.conf import HEALTH_CHECK


def get_status():
    results = []
    status_code = 200
    for check in HEALTH_CHECK:
        if check.exclude_main:
            continue
        status = check.health_status()
        results.append(status)
        status_code = max(status["code"], status_code)
    return results, status_code


class HealthCheckView(View):
    def get(self, request):
        results, status_code = get_status()
        return JsonResponse({"health": results}, status=status_code)


class HealthCheckInduvidualView(View):
    def get(self, request, health):
        status = health.health_status()
        status_code = status["code"]
        return JsonResponse({"health": status}, status=status_code)


class StatusPage(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        return render(request, "healthy_django/index.html")

    def post(self, request):
        results, status_code = get_status()
        return JsonResponse({"health": results}, status=status_code)
