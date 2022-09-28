from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperSerializer
from .models import Super
from super_types.models import SuperType

# Create your views here.
@api_view(['GET'])
def supers_list(request):
    supers= Super.objects.all()
    serializer= SuperSerializer(Super, many=True)
    return Response(serializer.data)