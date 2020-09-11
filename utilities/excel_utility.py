import openpyxl


def get_row_count(file_name, sheet):
    workbook = openpyxl.load_workbook(filename=file_name)
    working_sheet = workbook[sheet]
    return working_sheet.max_row


def get_column_count(file_name, sheet):
    workbook = openpyxl.load_workbook(file_name=file_name)
    working_sheet = workbook[sheet]
    return  working_sheet.max_column


def read_cell_data(file_name, sheet, row_no, column_no):
    workbook = openpyxl.load_workbook(file_name=file_name)
    working_sheet = workbook[sheet]
    return working_sheet.cell(row=row_no, column=column_no).value


def write_data_to_cell(file_name, sheet, row_no, column_no, data):
    workbook = openpyxl.load_workbook(file_name=file_name)
    working_sheet = workbook[sheet]
    working_sheet.cell(row=row_no, column=column_no).value = data
    workbook.save(file_name)