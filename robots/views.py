from django.http import HttpResponse
from . workbook_manager import workbook_manager

# Create your views here.


def get_excel(request):
    response = HttpResponse(content=workbook_manager(),
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=weekly_robots.xlsx'
    return response
