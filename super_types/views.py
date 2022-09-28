from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperTypeSerializer
from .models import SuperType

# Create your views here.
@api_view(['GET'])
def super_types_list(request):
    super_types = SuperType.objects.all()

    return Response('ok')
