from turtle import position
import xlsxwriter
workbook = xlsxwriter.Workbook('may.xlsx')
worksheet= workbook.add_worksheet('My_sheet')

content = (["May Phyo","28","Odoo_Intern"],
           ["Aung Myat Thu","27","Odoo_Intern"], 
           ["Ye Zaw Oo","27","Odoo_Intern"] ,
           ["Thin Ei San",'27',"Odoo_Intern",],
           ["Wah Ko",'21',"Odoo_Intern"], 
           ["Zaw Htet Aung","27","Odoo_Intern"],
           ["Yo Nax","27","Odoo_Intern"],  
          )
row = 0
column = 0
for name,age,position in (content):
    worksheet.write(row, column, name)
    worksheet.write(row, column + 1, age)
    worksheet.write(row, column + 2, position)
    row += 1
#workbook.close()