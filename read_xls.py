from openpyxl import load_workbook

DEBUG = False
RUN_DEBUG = False
if __name__ == '__main__':
    RUN_DEBUG = True


def read_xlsx(filename, column_name):
    wb = load_workbook(filename)
    sheet = wb.sheetnames[0]
    table = wb[sheet]
    names = table[column_name]
    result = []
    for name_cell in names:
        name = name_cell.value
        if DEBUG:
            print(name)
        if name is not None:
            result.append(name)
    return result

if RUN_DEBUG:
    column_name = 'C'
    filename = 'Ostatki_DrimkasUchet_1.xlsx'
    res = read_xlsx(filename, column_name)
    print(res)
