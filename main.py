from fractal_math import testCoord
import PIL
from PIL import Image
import colorsys

imgname = "2.jpg"
size = 1920*2,1080*2
clr = "r"
max_iter = 100
scale = float(0.00001)
x,y = -0.7463, 0.1102

im = Image.new("RGB", size)
clr_inc = 255 / max_iter
colors = []
if clr == 'r':
	r = 255
	for element in range(0,max_iter):
		r -= clr_inc
		colors.append([r,0,0])

x = float(-(size[0]/2 - [1 if size[0]%2 == 0 else 0][0])*scale + x)
y = float((size[1]/2 - [1 if size[1]%2 == 0 else 0][0])*scale + y)
x_save = x


a = 0
b = 0
for element in range(0, size[1]):
	for element in range(0,size[0]):
		clrval = testCoord(max_iter, x, y)
		im.putpixel((a, b), tuple(colors[clrval-1]))
		a += 1
		x += scale
	a = 0
	x, y = x_save, y - scale
	b += 1
im.save(imgname)