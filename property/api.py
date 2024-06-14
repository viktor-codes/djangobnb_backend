from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes, authentication_classes

from .models import Property
from .serializers import PropertiesListSerializer


@api_view(["GET"])
@permission_classes([])
@authentication_classes([])
def properties_list(request):
    properties = Property.objects.all()
    serializer = PropertiesListSerializer(properties, many=True)

    return JsonResponse({
        "data": serializer.data,
    })