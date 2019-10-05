from rest_framework import status, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.http import JsonResponse


class HeadersRequest(views.APIView):
    def get(self, request, *args, **kwargs):
        data = {}
        file = "editor/data/headers.json"
        with open(file, 'r') as f:
            data = json.load(f)
    
        if request.method == 'GET':
            return Response(data, status=status.HTTP_201_CREATED)