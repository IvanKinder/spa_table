import json

from django.core import serializers
from django.http import JsonResponse
from django.views import View

from table.models import Appeal


class AppealsView(View):
    def get(self, request, *args, **kwargs):
        error = None
        data = None

        try:
            data = serializers.serialize('json', Appeal.objects.all())
        except Exception:
            pass

        return JsonResponse({
            'success': not error,
            'data': json.loads(data),
            'error': error
        })
