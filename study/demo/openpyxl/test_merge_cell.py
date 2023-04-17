import openpyxl

# 定义要操作的Excel文件名和要操作的工作表名称
file_name = 'test_create_workbook.xlsx'
sheet_name = 'hello'

# 定义需要合并的单元格范围
merge_range = 'B2:D3'


def merge_cells(file_name, sheet_name, merge_range):
    """
    合并Excel文件中指定工作表的单元格

    :param file_name: Excel文件名
    :param sheet_name: 工作表名称
    :param merge_range: 需要合并的单元格范围，如'B2:D5'
    :return:
    """
    # 打开Excel文件
    wb = openpyxl.load_workbook(file_name)

    # 获取要操作的工作表，如果不存在，则新建一个工作表
    ws = wb[sheet_name] if sheet_name in wb.sheetnames else wb.create_sheet(sheet_name)

    # 合并单元格
    ws.merge_cells(merge_range)
    # 合并后赋值
    ws[str(eval('merge_range[1:3]'))].value = 'hello world'

    # 冻结窗格
    ws.freeze_panes('A1')

    # 保存文件
    wb.save(file_name)
    wb.close()


if __name__ == '__main__':
    try:
        # 合并指定工作表位置的单元格
        merge_cells(file_name, sheet_name, merge_range)
        print(f'工作表"{sheet_name}"的单元格已合并。')
    except Exception as e:
        print('出现异常:', e)
