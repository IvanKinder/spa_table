import json
import math

from django.contrib.auth.models import User
from django.db import transaction, IntegrityError
from django.http import JsonResponse
from django.views import View

from table.models import Appeal


class AppealsView(View):
    def get(self, request, *args, **kwargs):
        pages_count = 0
        params = request.GET

        filter_by = params.get('filterBy').split('-')[0] if params.get('filterBy') else ''
        filter_by_eq = params.get('filterBy').split('-')[1] if params.get('filterBy') else ''
        order_by = params.get('orderBy') if params.get('orderBy') else ''
        search_num = params.get('search')
        page = params.get('page')

        try:
            data = Appeal.objects.all()

            if filter_by == 'status':
                data = data.filter(status=filter_by_eq)

            if order_by:
                data = data.order_by(order_by)

            if search_num and search_num != 'null':
                data = data.filter(number__contains=search_num)

            pages_count = math.ceil(data.count() / 10)

            data = data[(int(page)-1)*10:int(page)*10]

            data = [{'creator': User.objects.get(pk=value['creator_id']).username, **value} for value in
                    list(data.values())]

        except Exception as e:
            data = str(e)

        return JsonResponse({
            'data': data,
            'pagesCount': pages_count
        })

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        appeal_number = body.get('appealNumber')
        description = body.get('description')
        data = []

        if appeal_number and description:
            try:
                with transaction.atomic():
                    new_appeal = Appeal(number=appeal_number, description=description, creator=User.objects.get(pk=1))
                    new_appeal.save()
                    data = str(new_appeal.number)
            except IntegrityError as e:
                data = str(e)
            except Exception as e:
                data = str(e)

        return JsonResponse({
            'data': data
        })
