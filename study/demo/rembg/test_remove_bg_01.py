from rembg import remove
from PIL import Image

# input_path = 'test_png/input.png'
input_path = 'test_png/2.png'
out_path = 'out_put/output-2.png'
input_img = Image.open(input_path)
out_put_img = remove(input_img)
out_put_img.save(out_path)