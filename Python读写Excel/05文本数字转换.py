import openpyxl


wb=openpyxl.Workbook()

ws=wb.active
ws.append(['文本','数字'])

ws['A2']='520'
ws['B2']=520

wb.save('文本数字.xlsx')