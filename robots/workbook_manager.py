from django.db.models import Count
from . models import Robot
from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook
from datetime import datetime, timedelta, timezone


def workbook_manager():
    robots = Robot.objects.filter(created__gte=datetime.now(
        timezone.utc) - timedelta(days=7)).values(
        'model', 'version').annotate(count=Count('serial'))
    robots_grouped = dict()
    for robot in robots:
        if robot['model'] in robots_grouped:
            robots_grouped[robot['model']].append(robot)
        else:
            robots_grouped[robot['model']] = [robot]
    wb = Workbook()
    for model in robots_grouped:
        ws = wb.create_sheet(model)
        ws.append(('Модель', 'Версия', 'Количество за неделю'))
        for serial in robots_grouped[model]:
            ws.append(list(serial.values()))
    del wb['Sheet']
    return save_virtual_workbook(wb)
