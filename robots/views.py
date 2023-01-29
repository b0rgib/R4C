from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import RobotSerializer
from . models import Robot
from rest_framework import status


@api_view(['POST'])
def add(request):
    serializer = RobotSerializer(data=request.data)
    if serializer.is_valid():
        model = serializer['model'].value
        version = serializer['version'].value
        serial = model + '-' + version
        created = serializer['created'].value
        robot = Robot(serial=serial, model=model,
                      version=version, created=created)
        robot.save()
        return Response(status=status.HTTP_200_OK)
    return Response(data='Invalid request', status=status.HTTP_400_BAD_REQUEST)
