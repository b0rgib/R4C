from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import RobotSerializer
from . models import Robot
from rest_framework import status
from django.http import HttpResponse
from . workbook_manager import workbook_manager



def get_excel(request):
    response = HttpResponse(content=workbook_manager(),
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=weekly_robots.xlsx'
    return response


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
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
