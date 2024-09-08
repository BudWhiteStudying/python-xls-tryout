import openpyxl

# Step 1: Load the existing workbook and access the sheet
existing_workbook = openpyxl.load_workbook('existing.xlsx')
sheet = existing_workbook['A sheet']

# Step 2: Read the values from cells B2 and D2
value_b2 = sheet['B2'].value
value_d2 = sheet['D2'].value

# Ensure the values are numeric (int or float) before summing them
if isinstance(value_b2, (int, float)) and isinstance(value_d2, (int, float)):
    total_sum = value_b2 + value_d2
else:
    raise ValueError("The values in cells B2 and D2 must be numeric.")

# Step 3: Create a new workbook
new_workbook = openpyxl.Workbook()
results_sheet = new_workbook.active
results_sheet.title = "Results"

# Step 4: Write the sum into cell A2 of the new sheet
results_sheet['B2'] = 'Sum:'
results_sheet['C2'] = total_sum

# Step 5: Save the new workbook as 'generated.xlsx'
new_workbook.save('generated.xlsx')

print("The sum of B2 and D2 has been written to 'generated.xlsx' in cell A2.")
