from rest_framework.decorators import api_view
from rest_framework.response import Response
from discord_app.models import Room
from .serializers import RoomSearializers

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSearializers(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRoom(request,pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSearializers(room, many=False)
    return Response(serializer.data)