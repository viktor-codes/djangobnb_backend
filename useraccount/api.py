from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes, authentication_classes


from .models import User
from .serializers import UserDetailSerializer

from property.serializers import ReservationsListSerializer


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def landlord_detail(request, pk):
    user = User.objects.get(pk=pk)

    serializer = UserDetailSerializer(user, many=False)
    return JsonResponse(serializer.data)


@api_view(['GET'])
def reservations_list(request):
    reservations = request.user.reservations.all()
    serializer = ReservationsListSerializer(reservations, many=True)
    
    return JsonResponse(serializer.data, safe=False)
