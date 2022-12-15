MOHAMMED SHAROOQ N
20220062
CSB S5


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
	glBegin(GL_LINES)
	glVertex2f(0,0)
	glVertex2f(100,0)
	glEnd()
	glFlush()
		
glutInit()
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(50, 50)
glutCreateWindow("Point")
glutDisplayFunc(plot_points)
clearScreen()
glutMainLoop()
