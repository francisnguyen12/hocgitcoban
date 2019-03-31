 from datetime import datetime
 import xlsxwriter

 # Create a workbook and add a worksheet.
 workbook = xlsxwriter.Workbook('Expenses03.xlsx')
 worksheet = workbook.add_worksheet()

 # Add a bold format to use to highlight cells.
 bold = workbook.add_format({'bold': 1})
222222222222
 # Add a number format for cells with money.
 money_format = workbook.add_format({'num_format': '$#,##0'})
1111111111
 # Add an Excel date format.
 date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})

 # Adjust the column width.
 worksheet.set_column(1, 1, 15)
 
 Add Pre-Master 001