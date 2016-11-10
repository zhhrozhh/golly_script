from PIL import Image
from math import floor
from sys import path
from sys import argv
from config0 import *
path.append(xdir[:-1])

f = open(xdir+'config2.py')
exec(f.read())
f.close()
f = open(xdir+'config3.py')
exec(f.read())
f.close()
ims = []
xx = 0

if argv[1] == 'e':
	l.reverse()
for cells in l:
	xx+=1
	img = Image.new('L',(bound[2],bound[3]))
	m = int(floor(len(cells)/2)*2)
	for i in range(0,m,2):
		x = cells[i]
		y = cells[i+1]
		img.putpixel((x,y),(255,255,255))

	img.save('/Users/zhangh40/Downloads/golly-2.8-mac/X0/'+argv[1]+str(xx)+'.png')
log.close()