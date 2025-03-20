from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Produce
from .serializers import ProduceSerializer, TransactionSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def list_produce(request):
    serializer = ProduceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def buy_produce(request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_all_produce(request):
    produce = Produce.objects.all()
    serializer = ProduceSerializer(produce, many=True)
    return Response(serializer.data)