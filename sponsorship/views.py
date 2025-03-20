from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import SponsorshipSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sponsor(request):
    serializer = SponsorshipSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)
