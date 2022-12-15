import OpenGL
import time
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
	triangle(0,0,1)
	x= int(input("enter transalation of origin for x factor"));
	y= int(input("enter transalation for origin y"));
	s= int(input("enter scaling factor"));
	glColor3f(1,0,1)
	triangle(x,y,s)
	glFlush()


def triangle(x,y,s):
	glBegin(GL_POLYGON)
	glVertex2f(x,y)
	glVertex2f((x+50)*s,(y+100)*s)
	glVertex2f((x+100)*s,y*s)
	glEnd()
	
def screen():
	glColor3f(1,1,1)
	glBegin(GL_POLYGON)
	glVertex2f(-500,-500)
	glVertex2f(-500,500)
	glVertex2f(500,500)
	glVertex2f(500,-500)
	glEnd()
	
		
glutInit()
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(50, 50)
glutCreateWindow("Point")
glutDisplayFunc(plot_points)
clearScreen()
glutMainLoop()
