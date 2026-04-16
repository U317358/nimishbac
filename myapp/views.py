

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserFormSerializer

@api_view(['POST'])
def submit_form(request):
    serializer = UserFormSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Data saved successfully"})
    
    return Response(serializer.errors)
    

    