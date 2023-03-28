import os, shutil, re

# 创建一个正则表达式匹配日期
datePattern = re.compile(r"""^(.*?) # 文本开头部分
((0|1)?\d)- # 月份
((0|1|2|3)?\d)- # 日期
((19|20)\d\d) # 年份
(.*?)$ # 文本结尾部分
""", re.VERBOSE)

# 遍历目录名称
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # 跳过没有日期的文件
    if mo is None:
        continue
    # 获取文件名的不同部分
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    datePattern = re.compile(r"""^(1) # all text before the date
    (2 (3) )- # one or two digits for the month
    (4 (5) )- # one or two digits for the day
    (6 (7) ) # four digits for the year
    (8)$ # all text after the date
    """, re.VERBOSE)
    # --snip--
    # 欧洲风格表单.
    euroFilename = beforePart + yearPart + '-' + monthPart + '-' + dayPart + afterPart
    print(f'euroFilename "{euroFilename}" ')
    # 获取全部绝对路径.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    print(f'amerFilename "{amerFilename}" ')
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    print(f'euroFilename "{euroFilename}" ')
    # 重命名文件.
    # print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    shutil.move(amerFilename, euroFilename)  # 测试后取消注释
    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
