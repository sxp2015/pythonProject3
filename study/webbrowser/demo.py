import webbrowser, sys, pyperclip

# webbrowser.open('https://www.baidu.com')

if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])

    print('address', address)
else:
    address = pyperclip.paste()

# 从剪切板读取路径，并拼接打开网址
webbrowser.open('https://cn.bing.com/' + address)
