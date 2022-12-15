import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

def clearScreen():
	glClearColor(1, 1, 1.0, 1)
	gluOrtho2D(-500, 500,-500,500)

def plot_points():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glColor3f(1,0,0) 
	#ellipse(0,0,50,100)
	#cube()
	background()
	monitor()
	windowslogo()
	glFlush()
	
def monitor():
	glColor3f(0,0,0.0)
	glPointSize(20.0)
	x=400
	y=250
	bezel=10
	
	glBegin(GL_LINE_LOOP)
	glVertex2f(-(x/2)-bezel, -(y/2)-bezel)
	glVertex2f(-(x/2)-bezel,(y/2)+bezel )	
	glVertex2f((x/2)-bezel, (y/2)-bezel)
	glVertex2f((x/2)-bezel,-(y/2)+bezel)
	glEnd()
	
	
	glBegin(GL_POLYGON)
	glVertex2f(-(x/2), -(y/2))
	glVertex2f(-(x/2),(y/2) )
	glVertex2f((x/2)-(2*bezel),(y/2)-(2*bezel) )
	glVertex2f((x/2)-(2*bezel), -(y/2)+(2*bezel))
	glEnd()
	
def windowslogo():
	glColor3f(0.1,0.1,0.9)
	glPointSize(20.0)
	x=40
	offset=0
	
	glBegin(GL_QUADS)  
	glVertex2f(-x-offset, -x-offset)
	glVertex2f(-x-offset,x+offset )	
	glVertex2f(x+offset, x+offset)
	glVertex2f(x+offset,-x-offset)
	glEnd()
	
	glColor3f(0,0,0)
	glBegin(GL_LINES)
	glVertex2f(x,0)
	glVertex2f(-x,0)	
	
	glVertex2f(0,x)
	glVertex2f(0,-x)
	glEnd()
	
def background():
	glColor3f(0.1,0.1,0.9)
	
def circle(posx,posy):   
	glColor3f(0,0,0)   
	sides = 32    
	radius = 100  
	glBegin(GL_POLYGON)    
	for i in range(100):    
		cosine= radius * cos(i*2*pi/sides) + posx    
		sine  = radius * sin(i*2*pi/sides) + posy    
		glVertex2f(cosine,sine)
	glEnd()
	
verticies = (
    (10, -10, -10),
    (10, 10, -10),
    (-10, 10, -10),
    (-10, -1, -1),
    (10, -1, 1),
    (10, 1, 1),
    (-10, -1, 1),
    (-10, 1, 1)
    )

edges = (
    (0,10),
    (0,30),
    (0,40),
    (20,10),
    (20,30),
    (20,70),
    (60,30),
    (60,40),
    (60,70),
    (50,10),
    (50,40),
    (50,70)
    )


def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def ellipse(xc,yc,rx,ry):
	x=0;
	y=ry;
	
	d1=((ry*ry)-(rx*rx*ry)+(0.25*rx*rx));
	dx = 2 * ry * ry * x;
	dy = 2 * rx * rx * y;
    
	while(dx<dy):
		glBegin(GL_POINTS)
		glVertex2f(x+xc,y+yc)
		glVertex2f(-x+xc,y+yc)
		glVertex2f(x+xc,-y+yc)
		glVertex2f(-x+xc,-y+yc)
		glEnd()
		
		if(d1<0):
			x+=1;
			dx=dx+(2*ry*ry);
			d1=d1+dx+(ry*ry);
		else:
			x+=1;
			y-=1;
			dx = dx + (2 * ry * ry);
			dy = dy - (2 * rx * rx);
			d1 = d1 + dx - dy + (ry * ry);
	
	d2=(((ry*ry)*((x+0.5)*(x+0.5)))+((rx*rx)*((y-1)*(y-1)))-(rx*rx*ry*ry));
	
	while(y>=0):
		glBegin(GL_POINTS)
		glVertex2f(x+xc,y+yc)
		glVertex2f(-x+xc,y+yc)
		glVertex2f(x+xc,-y+yc)
		glVertex2f(-x+xc,-y+yc)
		glEnd()
		
		if(d2>0):
			y-=1;
			dy=dy-(2*rx*rx);
			d2=d2+(rx*rx)-dy;
		else:
			y-=1;
			x+=1;
			dx = dx + (2 * ry * ry);
			dy = dy - (2 * rx * rx);
			d2 = d2 + dx - dy + (rx * rx);

def setpixel(a,b,color):
	glBegin(GL_POINTS)
	glVertex2f(a,b)
	glEnd()

def getpixel(a,b):
	color=glReadPixels(a,b,1,1,GL_RGB,GL_FLOAT)
	return color 
		
def floodfill(x,y,fill,old):
	if getpixel(x,y)==old:
		setpixel(x,y,fill)
		floodfill(x+1,y,fill,old)
		floodfill(x-1,y,fill,old)
		floodfill(x,y+1,fill,old)
		floodfill(x,y-1,fill,old)
	
floodfill(0,0,1,0)
		
glutInit()
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(50, 50)
glutCreateWindow("Point")
glutDisplayFunc(plot_points)
clearScreen()
glutMainLoop()
