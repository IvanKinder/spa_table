import json

from django.core import serializers
from django.http import JsonResponse
from django.views import View

from table.models import Appeal


class AppealsView(View):
    def get(self, request, *args, **kwargs):
        error = None
        data = ''
        params = request.GET
        filter_param = params['filter']
        search_param = params['search']

        try:
            if filter_param:
                if filter_param in ['created_at', 'status']:
                    data = serializers.serialize('json', Appeal.objects.order_by(filter_param))
                else:
                    data = serializers.serialize('json', Appeal.objects.filter(status=int(filter_param)))
            elif search_param:
                data = serializers.serialize('json', Appeal.objects.filter(number__contains=search_param))
            else:
                data = serializers.serialize('json', Appeal.objects.all())
        except Exception:
            pass

        print(data)

        return JsonResponse({
            'success': not error,
            'data': json.loads(data),
            'error': error
        })
