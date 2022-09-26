# XlsxWriter
> XlsxWriter is a Python module for creating Excel files.

### Advantages
   - Supports more Excel features than any of alternative modules
   - Excel file ထုတ်ပေးတာနဲ့ 100%  တူ
   - Files and Tests တို့လို extensive documents ရှိ
   - အလုပ်လုပ်ပုံမြန်ဆန်ပီးတော့ Large output files များကိုပင် memory နည်းနည်းနဲ့သုံးရန် configure လုပ်နိုင်

### Disadvantages
   - Cannot `READ` or `MODIFY` existing Excel XLSX files

> XlsxWriter support features
   - Formatting, images, charts, page setup, autofilters, conditional formatting and many others

> XlsxWriter Installation
   - activate virtual environment and add python interpreter
   - type `-pip install xlsxwriter` on cmd or VS Code's Terminal cmd
   - after installation successful, you can write `XLSX` file with Python

> Running Sample Program
   - 1st step => `import xlsxwriter`
     to use xlsx features 
   - create new WorkBook Object using `Workbook()` Constructor
     - eg
        ```
        workbook = xlsxwriter.Workbook('name.xlsx')
        ```
   - Workbook Object ကိုအသုံးပြုပီး ကို create လုပ်ချင်တဲ့ Sheet ကို add_worksheet() method ကနေတစ်ဆင့် create လုပ်
     - eg
       ```
       worksheet = workbook.add_worksheet('sheet_name')
       ```
     - ကိုကြိုက်တဲ့ Sheet_name ပေးလို့ရ
     - Default အနေနဲ့ Sheet1, Sheet2, Sheet3, etc... 
     - WorkSheet ထဲ data များထည့်ရန် .write() method သုံး
     - Syntax
        ```
        worksheet.write(row, col, data)
        ```

   - Some data we want to write to the worksheet
     - eg
        ```
        expenses = (
            ['Rent',100000],
            ['Gas',3000],
            ['Food',50000],
            ['Gym',20000],
        )
        ```
   - ထည့်လိုက်တဲ့ အပေါ်က data တွေက col0, col1 မှာ နေရာယူသွားမှာဖြစ်
   - Rows and Cols တွေက index 0  ကနေ စပါတယ်
   - ပထမဆုံး cell ကွက်ကနေ data စထည့်
     - eg
        ```
        row = 0
        col = 0
        ```
   - Data တွေကို row_by_row တစ်ခုချင်းဆီ ဆွဲထုတ်ပီး သွင်းဖို့အတွက် For Loop ပတ်
     - eg
       ```
       for item, cost in (expenses):
          worksheet.write(row, col,     item)
          worksheet.write(row, col + 1, cost)
          row += 1
       ```
   - အပေါ်တွင် col ၂ ခုစာ data ထည့်ခဲ့သည့်အတွက် col + 1 အထိပဲ ရှိ
   - Formula  သုံးပီး Total တွက်
     - eg
       ```
       worksheet.write(row, 0, 'Total')
       worksheet.write(row, 1, '=SUM(B1:B4)')
       ```
   - =SUM(B1:B4) သည် col B1 ကနေ B4 အထိ ပေါင်းပေးမှာဖြစ်တယ်
   - Close your workbook after all operation.
     - syntax
        ```
        workbook.close()
        ```

> Run you file
   - type `python yourfile.py` 
   - file will run .xlsx format on your project folder
       