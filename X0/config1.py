from PIL import Image
from sys import argv
from config0 import *
pic_addr = argv[1]
x0 = Image.open(pic_addr)

x1 = x0.convert('L')
x2 = x1.point(lambda x: 255*int(x>125),'1')
x2.save(xdir+'s0.png')
sz = x2.size
f = open(xdir+'config2.py','w')
f.write('bound = [0,0,')
f.write(str(x2.size[0]))
f.write(',')
f.write(str(x2.size[1]))
f.write(']\n')
f.write('d = '+argv[2]+'\n')

f.close()