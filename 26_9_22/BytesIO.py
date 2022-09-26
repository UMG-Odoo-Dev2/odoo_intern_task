from io import BytesIO
import xlsxwriter

output = BytesIO()
workbook = xlsxwriter.Workbook(output)
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello')
workbook.close()

xlsx_data = output.getvalue()