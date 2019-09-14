from django.views import View
from django.http import JsonResponse

from .graphql import schema


class GraphQLView(View):

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')
        result = schema.execute(search)
        return JsonResponse(result.data, safe=False)
