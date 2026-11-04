from pathlib import Path
from openpyxl import load_workbook
from datetime import datetime

#read excell sheet
workbook = load_workbook(r"F:\Guvi\Login_Data.xlsx")
sheet=workbook["Sheet1"]

def read_test_data():
    test_data = []
    for row in range(2,sheet.max_row+1):
        test_id = sheet.cell(row,1).value
        username = sheet.cell(row, 2).value
        password = sheet.cell(row, 3).value or ""
        tester= sheet.cell(row, 6).value
        test_data.append([row,test_id,username,password,tester])

    return test_data

def write_result(row,result,tester):

    now = datetime.now()
    sheet.cell(row,4).value=now.strftime("%d/%m/%Y")
    sheet.cell(row,5).value=now.strftime("%H:%M:%S")
    sheet.cell(row,6).value=tester
    sheet.cell(row,7).value=result

    workbook.save(r"F:\Guvi\Login_Data.xlsx")
