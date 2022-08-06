import openpyxl as xl
from datetime import date, time, datetime, timedelta

def createSpreadsheet():
    wb = xl.load_workbook('desert_fortresses.xlsx')
    ws = wb.active
    ws.append(["coord X", "coord Y", "hours", "minutes", "seconds", "free in"])

def updateSpreadsheet(coord_x, coord_y, hours = 0, minutes = 0, seconds = 0):
    wb = xl.load_workbook('desert_fortresses.xlsx')
    ws = wb.active
    free_in = datetime.today() + timedelta(hours = hours, minutes = minutes, seconds = seconds)
    ws.append([coord_x, coord_y, hours, minutes, seconds, free_in.strftime('%H:%M:%S')])
    wb.save('desert_fortresses.xlsx')