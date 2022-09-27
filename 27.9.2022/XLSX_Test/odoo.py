import xlsxwriter
workbook=xlsxwriter.Workbook('odoo.xlsx')
worksheet=workbook.add_worksheet('Odoo Intern')

bold=workbook.add_format({'bold':1}) #Headings

merge=workbook.add_format({'bold':1,'align':'center','valign':'venter'}) #Title

worksheet.merge_range('A1:D1',"Odoo Intern",merge)

worksheet.set_column('A:D',26)

index=1
head=['Name','Address','Phone Number','Email']

for cell in range(65,69):
    worksheet.write(chr(cell)+str(2),head[index-1],bold)
    index+=1

row=2
col=0

person=(
    ['Aung Myat Thu','Yangon','09-964478776','aungmyatthu@gmail.com'],
    ['Ye Zaw Oo','Yangon','09-968356673','yezawoo@gmail.com'],
    ['Zaw Thu Htet','Yangon','09-400454567','zawthuhtet@gmail.ocm'],
    ['Phyoe Wai Kyaw','Yangon','09-265789977','phyoewaikyaw@gmail.com'],
    ['Thin Ei San','Yangon','09-456677889','thineisan@gmail.com'],
    ['May Phyo Thu','Yangon','09-987654345','mayphyothu@gmail.com'],
    ['Wint Wah Ko','Yangon','09-984454345','wintwahko@gmail.com']
)
for name,address,phone,email in (person):
    worksheet.write(row,col,name)
    worksheet.write(row,col+1,address)
    worksheet.write(row,col+2,phone)
    worksheet.write(row,col+3,email)
    row+=1

workbook.close()