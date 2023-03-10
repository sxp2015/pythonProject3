# -*- coding: utf-8 -*-
# ⭐Python 60套学习资源：http://t.cn/A6xASARf
# 📱公众号 :程序员晚枫 读者交流群：http://www.python4office.cn/wechat-group/
# 🏠2022最新视频：1行代码，实现自动化办公：https://www.bilibili.com/video/BV1pT4y1k7FH


from PIL import Image
from xlsxwriter.workbook import Workbook


class ExcelPicture(object):
    FORMAT_CONSTRAINT = 65536

    def __init__(self, pic_file, ratio=0.5):
        self.__pic_file = pic_file

        self.__ratio = ratio
        self.__zoomed_out = False

        self.__formats = dict()

    # 缩小图片
    def zoom_out(self, _img):
        _size = _img.size
        _img.thumbnail((int(_img.size[0] * self.__ratio), int(_img.size[1] * self.__ratio)))

        self.__zoomed_out = True

    # 对颜色进行圆整
    def round_rgb(self, rgb, model):
        return tuple([int(round(x / model) * model) for x in rgb])

    # 查找颜色样式，去重
    def get_format(self, color):
        _format = self.__formats.get(color, None)

        if _format is None:
            _format = self.__wb.add_format({'bg_color': color})
            self.__formats[color] = _format

        return _format

    # 操作流程
    def process(self, output_file='_pic.xlsx', color_rounding=False, color_rounding_model=5.0):
        # 创建xlsx文件，并调整行列属性
        self.__wb = Workbook(output_file)
        self.__sht = self.__wb.add_worksheet()
        self.__sht.set_default_row(height=9)
        self.__sht.set_column(0, 5000, width=1)

        # 打开需要进行转换的图片
        _img = Image.open(self.__pic_file)
        print        ('Picture filename:', self.__pic_file)

        # 判断是否需要缩小图片尺寸
        if self.__ratio < 1:
            self.zoom_out(_img)

        # 遍历每一个像素点，并填充对应的颜色到对应的Excel单元格
        _size = _img.size
        print('Picture size:', _size)
        for (x, y) in [(x, y) for x in range(_size[0]) for y in range(_size[1])]:
            _clr = _img.getpixel((x, y))

            # 如果颜色种类过多，则需要将颜色圆整到近似的颜色上，以减少颜色种类
            if color_rounding: _clr = self.round_rgb(_clr, color_rounding_model)

            _color = '#%02X%02X%02X' % _clr
            self.__sht.write(y, x, '', self.get_format(_color))

        self.__wb.close()

        # 检查颜色样式种类是否超出限制，Excel2007对样式数量有最大限制
        format_size = len(self.__formats.keys())
        if format_size >= ExcelPicture.FORMAT_CONSTRAINT:
            print('Failed! Color size overflow: %s.' % format_size)
        else:
            print            ('Success!')
            print            ('Color: %s' % format_size)
            print            ('Color_rounding:', color_rounding)
            if color_rounding:
                print            ('Color_rounding_model:', color_rounding_model)


if __name__ == '__main__':
    r = ExcelPicture('111.jpg', ratio=0.5)
    r.process('0407.xlsx', color_rounding=True, color_rounding_model=5.0)