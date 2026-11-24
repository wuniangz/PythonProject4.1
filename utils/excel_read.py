import openpyxl
def get_data():
    if __name__ == '__main__':
        open_ex = openpyxl.load_workbook('../数据来源.xlsx')
    else:
        open_ex = openpyxl.load_workbook('./数据来源.xlsx')
    sheet = open_ex['Sheet1']
    data = []
    keys = [cell.value for cell in sheet[2]]
    for value in sheet.iter_rows(min_row=3, values_only=True):
        data.append(dict(zip(keys, value)))

    open_ex.close()
    return data
if __name__ == '__main__':
    print(get_data())




