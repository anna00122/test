import xlwt

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("sheet1")

sheet.write(0, 0, '자바')
sheet.write(0, 1, '메딥')
sheet.write(0, 2, '메23ㅈ')

sheet.write(1, 0, '파이썬')
sheet.write(1, 1, '에일린')

sheet.write(2, 0, 'C')
sheet.write(2, 1, '로키')

    ## 첫번째 인자가 행, 두번째 인자가 열

workbook.save("test.xlsx")
