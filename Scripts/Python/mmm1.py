from subprocess import call
import golly as g
import sys
from config0 import *
for se in range(2):
	pic_addr = xdir+g.getstring('pic addr\n')
	d = g.getstring('d\n')
	call([py3,xdir+'config1.py',pic_addr,str(d)])
	sys.path.append(xdir[:-1])
	x = open(xdir+'config2.py')
	exec(x.read())
	x.close()

	g.open(xdir+'s0.png')
	g.setrule("b3/s23")
	f = open(xdir+'config3.py','w')
	f.write('l=[]\n')
	for i in xrange(d):
		g.run(1)
		g.update()
		cells = g.getcells(bound)
		f.write('l.append('+str(cells)+')\n')
	f.close()
	call([py3,xdir+'config4.py','e' if se else 's'])
interd =  int(g.getstring('inter d\n'))
call([py3,xdir+'bridge.py',xdir+'s'+str(d)+'.png',xdir+'e1.png',str(interd)])
