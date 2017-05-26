from mandelbrot_math import testCoord
import PIL
from PIL import Image

size = 100,100
clr = "r"
max_iter = 50
scale = float(0.01)

im = Image.new("RGB", size)
clr_inc = 255 / max_iter
colors = []
if clr == 'r':
	r = 255
	for element in range(0,max_iter):
		r -= clr_inc
		colors.append([r,0,0])

x = -(size[0]/2 - [.5 if size[0]%2 == 0 else 0][0])
y = (size[1]/2 - [.5 if size[1]%2 == 0 else 0][0])
a = 0
b = 0
for element in range(0, size[1]):
	for element in range(0,size[0]):
		clrval = testCoord(max_iter, x, y)
		im.putpixel((a,b), colors[clrval])
		a += 1
	b += 1