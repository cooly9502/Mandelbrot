from fractal_math import testCoord
import PIL
from PIL import Image
import colorsys
import math
sq = lambda x : x * x
genClr = False

imgname = "test.jpg"
size = 500,500
clr = "r"
max_iter = 255
scale = float(0.000001)
x,y = float(0.281717921930775), float(0.5771052841488505)

im = Image.new("RGB", size)
clr_inc = 255 / max_iter
colors = []

if clr == 'r':
	r = 255
	for element in range(0,max_iter):
		r -= clr_inc
		colors.append([r,0,0])
if clr == 'b':
	b = 0
	for element in range(0,max_iter):
		b += clr_inc
		colors.append([0,0,b])
if clr == 'random1':
	#Verifys that colors are to be generated
	genClr = True

def genColor(n):
	r = int( math.fabs( 255 % (n*math.sin(n) )) )
	g = int( math.fabs( 255 % sq(n) ) )
	b = int( math.fabs( 255 % n ) )
	return [r, g, b]

x = float(-(size[0]/2 - [1 if size[0]%2 == 0 else 0][0])*scale + x)
y = float((size[1]/2 - [1 if size[1]%2 == 0 else 0][0])*scale + y)
x_save = x


a = 0
b = 0
for element in range(0, size[1]):
	for element in range(0,size[0]):
		clrval = testCoord(max_iter, x, y)
		if genClr == True:
			seed = clrval
			clrval = genColor(seed)
			clrval = tuple(clrval)
		else:
			clrval = colors[clrval - 1]
			clrval = tuple(clrval)
		im.putpixel((a, b), clrval)
		a += 1
		x += scale
	a = 0
	x, y = x_save, y - scale
	b += 1
im.save(imgname)
im.show()