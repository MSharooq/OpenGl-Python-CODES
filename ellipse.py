from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
def init():
	glClearColor(0.0, 0.0, 0.0, 1.0)
	gluOrtho2D(-300, 300, -300, 300)

def plotLine(x1, y1, x2, y2):
	deltaX = x2 - x1
	deltaY = y2 - y1
	steps = 0
	
	if (abs(deltaX) > abs(deltaY)):
		steps = abs(deltaX)
	else:
		steps = abs(deltaY)
	Xincrement = deltaX / steps
	Yincrement = deltaY / steps
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0, 0.0, 0.0)
	glPointSize(10.0)
	glBegin(GL_POINTS)
	
	for step in range(1, steps + 1):
		glVertex2f(round(x1), round(y1))
		x1 = x1 + Xincrement
		y1 = y1 + Yincrement
	glEnd()
	glFlush()

def midptellipse(rx, ry, xc, yc):
 
    x = 0;
    y = ry;
 
    # Initial decision parameter of region 1
    d1 = ((ry * ry) - (rx * rx * ry) +
                      (0.25 * rx * rx));
    dx = 2 * ry * ry * x;
    dy = 2 * rx * rx * y;
 
    # For region 1
    while (dx < dy):
 
        # Print points based on 4-way symmetry
		glBegin(GL_POINTS)
			glVertex2f(x + xc,y + yc)
			glVertex2f(-x + xc,y + yc)
			glVertex2f(x + xc,-y + yc)
			glVertex2f(-x + xc,-y + yc)
		glEnd()
        # Checking and updating value of
        # decision parameter based on algorithm
        if (d1 < 0):
            x += 1;
            dx = dx + (2 * ry * ry);
            d1 = d1 + dx + (ry * ry);
        else:
            x += 1;
            y -= 1;
            dx = dx + (2 * ry * ry);
            dy = dy - (2 * rx * rx);
            d1 = d1 + dx - dy + (ry * ry);
 
    # Decision parameter of region 2
    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
          ((rx * rx) * ((y - 1) * (y - 1))) -
           (rx * rx * ry * ry));
 
    # Plotting points of region 2
	while (y >= 0):
 
        # printing points based on 4-way symmetry
		glBegin(GL_POINTS)
			glVertex2f(x + xc,y + yc)
			glVertex2f(-x + xc,y + yc)
			glVertex2f(x + xc,-y + yc)
			glVertex2f(-x + xc,-y + yc)
		glEnd()
 
        # Checking and updating parameter
        # value based on algorithm
		if (d2 > 0):
			y -= 1;
			dy = dy - (2 * rx * rx);
			d2 = d2 + (rx * rx) - dy;
		else:
			y -= 1;
			x += 1;
			dx = dx + (2 * ry * ry);
			dy = dy - (2 * rx * rx);
			d2 = d2 + dx - dy + (rx * rx);

midptellipse(100, 50, 0, 0)

def main():
	print ("Enter following coordinates for a line :")
	x1 = int(input("Enter x1: "))
	y1 = int(input("Enter y1: "))
	x2 = int(input("Enter x2: "))
	y2 = int(input("Enter y2: "))
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(0, 0)
	glutCreateWindow("Plot Line using DDA")
	glutDisplayFunc(lambda: plotLine(x1, y1, x2, y2))
	glutIdleFunc(lambda: plotLine(x1, y1, x2, y2))
	init()
	glutMainLoop()
main()
