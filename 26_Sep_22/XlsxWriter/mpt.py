import xlsxwriter
workbook = xlsxwriter.Workbook('mpt.xlsx') 
worksheet = workbook.add_worksheet()
 
worksheet.write('A1','No')
worksheet.write('B1','Name')
worksheet.write('C1', 'Age')
worksheet.write('D1', 'Position')
worksheet.write('E1',"Company's Name")
worksheet.write('F1',"City")

workbook.close()
