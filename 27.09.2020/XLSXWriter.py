import XLSXWriter

workbook = XLSXWriter.workbook('odoo.xlsx')
worksheet = workbook.add_worksheet('data')

bold = workbook.add_format({'bold':1})

price_format = workbook.add_format({"num_format":"$#,##0"})
worksheet.set_column(1,1,10)

worksheet.write("A1","No.",bold)
worksheet.write("B1","Item",bold)
worksheet.write("C1","Quantity.",bold)
worksheet.write("D1","Unit_Price",bold)
worksheet.write("E1","Total_Price",bold)

fruits = (
    [1,'Apple',2,100],
    [2,'Orange',3,200],
    [3,'Mango',5,500]
)

row = 1
col = 0

for No,Item,Qty,UnitPrice in (fruits):
    worksheet.write_number(row,col,No)
    worksheet.write_string(row,col+1,Item)
    worksheet.write_number(row,col+2,Qty)
    worksheet.write_number(row,col+3,UnitPrice,price_format)
    worksheet.write_number(row,col+4,)
