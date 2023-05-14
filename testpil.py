from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

img = Image.open('test.jpg')
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("MetalMania-Regular.ttf", 100)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((100, 0),"Sample Text",(255,255,255),font=font)
img.save('sample-out.jpg')