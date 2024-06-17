from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes, authentication_classes


from .models import User
from .serializers import UserDetailSerializer


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def landlord_detail(request, pk):
    user = User.objects.get(pk=pk)

    serializer = UserDetailSerializer(user, many=False)
    return JsonResponse(serializer.data)
