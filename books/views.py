from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from django.http import JsonResponse
from .schema import schema


class CustomGraphQLView(GraphQLView):
	def dispatch(self, request, *args, **kwargs):
		if request.method == "OPTIONS":
			response = JsonResponse({})
		else:
			response = super().dispatch(request, *args, **kwargs)
		response["Access-Control-Allow-Origin"] = request.headers.get("Origin", "*")
		response["Access-Control-Allow-Credentials"] = "true"
		response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
		response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
		return response

graphql_view = csrf_exempt(CustomGraphQLView.as_view(graphiql=True, schema=schema))
