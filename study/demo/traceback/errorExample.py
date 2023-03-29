import traceback

try:
    raise Exception('这是一个错误日志')
except RuntimeError:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('错误日志写入到 errorInfo.txt.')
