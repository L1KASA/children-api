from django.http import JsonResponse, HttpRequest
from django.views import View
from .services import ChildService


class ChildrenView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        try:
            children_data = ChildService.get_all_children()

            return JsonResponse({
                'success': True,
                'children': children_data,
                'count': len(children_data)
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': 'Ошибка при получении данных',
                'detail': str(e)
            },
            status=500,
        )
