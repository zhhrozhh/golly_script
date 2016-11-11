from PIL import Image
from sys import argv
from config0 import *
if __name__ == '__main__':
	sp = Image.open(argv[1])
	ep = Image.open(argv[2])
	fs = int(argv[3])
	s = sp.load()
	e = ep.load()
	for i in range(fs):
		img = Image.new('L',sp.size)
		for x in range(sp.size[0]):
			for y in range(sp.size[1]):
				if x%fs == i or y%fs == i:
					img.putpixel((x,y),(0,0,0))
					s[x,y] = (0,0,0)
				else:
					img.putpixel((x,y),s[x,y])
		img.save(xdir+'t'+str(i)+'.png')
	for i in range(fs):
		img = Image.new('L',sp.size)
		for x in range(sp.size[0]):
			for y in range(sp.size[1]):
				if x%fs == i or y%fs == i:
					img.putpixel((x,y),e[x,y])
		img.save(xdir+'m'+str(i)+'.png')

