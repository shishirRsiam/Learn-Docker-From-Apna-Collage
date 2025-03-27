from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

database = {
    'name': []
}

class TestApiView(APIView):
    def get(self, request, format=None):
        content = {
            'status': 'success',
            # 'data': database,
            'count_name': len(database['name']),
            'name': database['name'],
        }
        return Response(content, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        name = request.data.get('name', None)
        if name:
            database['name'].append(name)
            response = {
                'status': 'success',
                'message': 'Name saved successfully'
            }
            return Response(response, status=status.HTTP_200_OK)
        response = {
            'status': 'error',
            'message': 'Name field is required'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
