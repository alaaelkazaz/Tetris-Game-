''' General Comments :

 program : Tetrisfinal.py
 Interpreter : python 3.7
 Authors:
 Rania Dawood
 Alaa Elkzaz
 Hanan Ahmed
 Mohammed Morad
 Comments:
  to start without the starting theme set the flag start_background to zero

  '''
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import randrange as rand
import random
import pygame
from array import *
import time
from numpy import *



################################################################################################################################################################
#global varibles

# Score , Goal , level
score=7
goal=300
level=1

#pick the shape
n = 2
currentshape = 0

#to define how mant rotates for the current shape should be done
rotate=0  

#color
x=1
chosencolor = 0

# timer render
level_time_sec=180
level_time_min=0
render_sec=0

# gameover flag
gameoverrt=0

#sounds
hit_sound=None
gameover_sound=None
lineremove_sound=None
music_sound=None
win_sound=None
control_sound=0
soundSrc=[music_sound,gameover_sound,hit_sound ,lineremove_sound,win_sound]

# starting theme make it 1 to appear in the beginning
start_background=1
# Window dimensions

# 16*10
width = 1000
height = 700

axrng = 1.0

# Time Interval
time_interval = 1000

# the arrows
deltap = 0.0
deltan = 0.0

#the drawing matrices
awidth = [-.96, -.86, -.76, -.66, -.56, -.46, -.36, -.26, -.16, -.06, .04,.14,.24,.34,.44,.54,.64,.74,.84,.94]
aheight = [-.885, -.798, -.708, -.618, -.528, -.438, -.348, -.258, -.168, -.078, .018, .108, .198, .288, .378, .468,
           .558, .648, .738, .828, .918, 1.008, 1.098, 1.188, 1.278, 1.368, 1.458, 1.548]
allshapes = []
allcolors = []


global texture

# represnts the game matrix
floor = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
# represents the color of each block represented in code with variable (x)
color = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


################################################################################################################################################################




##################################################################################################################################
#init function

def init():
    global texture
    glClearColor(0.0, 0.0, 0.0, 1.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Make axrng larger and see what happens!
    glOrtho(-axrng, axrng, -axrng, axrng, -axrng, axrng)
    glMatrixMode(GL_MODELVIEW)

    glEnable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glDisable(GL_DEPTH_TEST)

    texture = glGenTextures(9)  # generate all textures of the game

    #######################################################################################################
    # Create MipMapped Texture
    imgload = pygame.image.load("TetrisMain1.jpeg")  # the grid
    img = pygame.image.tostring(imgload, "RGBA", 1)  # 0) # Serializing the image to a string
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)  # GL_CLAMP)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)  # GL_CLAMP)
    # gluBuild2DMipmaps( target, internalFormat,  width,  height,  format, type,  raw_image)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)  # try this

    #######################################################################################################
    imgload = pygame.image.load("11.png")  # The purple
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[1])
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)  # GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)
    #######################################################################################################
    imgload = pygame.image.load("22.png")  # The yellow
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[2])
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)  # GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)
    #######################################################################################################
    imgload = pygame.image.load("33.png")  # The  red
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[3])
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)  # GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)
    #######################################################################################################
    imgload = pygame.image.load("44.png")  # The orange
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[4])
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)  # GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)
    #######################################################################################################
    imgload = pygame.image.load("55.png")  # The green
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[5])
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)  # GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)
    #######################################################################################################
    imgload = pygame.image.load("StartBack.png")  # The green --> T  shape
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[6])
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)  # GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)
    #######################################################################################################
    imgload = pygame.image.load("gameoverback.png")
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[7])
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)  # GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)
    #######################################################################################################
    imgload = pygame.image.load("winback.png")
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[8])
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)  # GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, img)
    #######################################################################################################
    # sounds of the game , must be in wav form
    pygame.mixer.init()
    soundSrc[0] = pygame.mixer.Sound("music.wav")
    soundSrc[1] = pygame.mixer.Sound("gameover1.wav")
    soundSrc[2] = pygame.mixer.Sound("force-hit.wav")
    soundSrc[3] = pygame.mixer.Sound("line-remove.wav")
    soundSrc[4]=pygame.mixer.Sound("success.wav")


##################################################################################################################################
#text and textures

def timer(v):
    global time_interval
    # supossed to change it for texture
    Display()
    glutTimerFunc(time_interval, timer, 1)

def level_time():
    global level_time_min
    global level_time_sec
    global render_sec
    level_time_min=level_time_sec//(60)
    render_sec=level_time_sec%(60)
    level_time_sec-=1
    glLoadIdentity()
    glLineWidth(4)  # Line with 3px
    glColor(1, 1, 1)  # white Color
    glLoadIdentity()
    glTranslate(.43, -.85, 0)
    glScale(.1 / 152.38, .1 / 152.38, .1 / 152.38)
    time1 = str(level_time_min)
    string3 = time1.encode()  # conversion from Unicode string to byte string
    for c in string3:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)
    
    glLoadIdentity()
    glTranslate(.52, -.85, 0)
    glScale(.1 / 152.38, .1 / 152.38, .1 / 152.38)
    time2 = str(render_sec)
    string4 = time2.encode()  # conversion from Unicode string to byte string
    for c in string4:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)

def draw_background():
    glColor3f(.5, .5, .5)
    # point 1
    x1 = -1
    y1 = 1

    # point 2
    x2 = 1
    y2 = 1

    # point 3
    x3 = -1
    y3 = -1

    # point 4
    x4 = 1
    y4 = -1
    glLoadIdentity()
    glEnable(GL_TEXTURE_2D)
    glColor3f(1, 1, 1)
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glBegin(GL_QUADS)

    glTexCoord(1, 0)
    glVertex(x4, y4)

    glTexCoord(0, 0)
    glVertex(x3, y3)

    glTexCoord(0, 1)
    glVertex(x1, y1)

    glTexCoord(1, 1)
    glVertex(x2, y2)

    glEnd()
    glDisable(GL_TEXTURE_2D)

def draw_start():
    glColor3f(.5, .5, .5)
    # point 1
    x11 = -1
    y11 = 1

    # point 2
    x22 = 1
    y22 = 1

    # point 3
    x33 = -1
    y33 = -1

    # point 4
    x44 = 1
    y44 = -1

    # Drawing Horizontal lines upper half
    glLoadIdentity()
    glEnable(GL_TEXTURE_2D)
    glColor3f(1, 1, 1)
    glBindTexture(GL_TEXTURE_2D, texture[6])
    glBegin(GL_QUADS)

    glTexCoord(1, 0)
    glVertex(x44, y44)

    glTexCoord(0, 0)
    glVertex(x33, y33)

    glTexCoord(0, 1)
    glVertex(x11, y11)

    glTexCoord(1, 1)
    glVertex(x22, y22)

    glEnd()
    glDisable(GL_TEXTURE_2D)

def draw_gameover():
    glColor3f(.5, .5, .5)
    # point 1
    x111 = -1
    y111 = 1

    # point 2
    x222 = 1
    y222 = 1

    # point 3
    x333 = -1
    y333 = -1

    # point 4
    x444 = 1
    y444 = -1

    # Drawing Horizontal lines upper half
    glLoadIdentity()
    glEnable(GL_TEXTURE_2D)
    glColor3f(1, 1, 1)
    glBindTexture(GL_TEXTURE_2D, texture[7])
    glBegin(GL_QUADS)

    glTexCoord(1, 0)
    glVertex(x444, y444)

    glTexCoord(0, 0)
    glVertex(x333, y333)

    glTexCoord(0, 1)
    glVertex(x111, y111)

    glTexCoord(1, 1)
    glVertex(x222, y222)

    glEnd()
    glDisable(GL_TEXTURE_2D)

def draw_win():
    glColor3f(.5, .5, .5)
    # point 1
    xn = -1
    yn = 1

    # point 2
    xnn = 1
    ynn = 1

    # point 3
    xn1 = -1
    yn1 = -1

    # point 4
    xn2 = 1
    yn2 = -1

    glLoadIdentity()
    glEnable(GL_TEXTURE_2D)
    glColor3f(1, 1, 1)
    glBindTexture(GL_TEXTURE_2D, texture[8])
    glBegin(GL_QUADS)

    glTexCoord(1, 0)
    glVertex(xn2, yn2)

    glTexCoord(0, 0)
    glVertex(xn1, yn1)

    glTexCoord(0, 1)
    glVertex(xn, yn)

    glTexCoord(1, 1)
    glVertex(xnn, ynn)

    glEnd()
    glDisable(GL_TEXTURE_2D)

def draw_score():
    global score
    glLoadIdentity()
    glLineWidth(4)  # Line with 3px
    glColor(1, 1, 1)  # white Color
    glLoadIdentity()
    glTranslate(.4, -.57, 0)
    glScale(.1 / 152.38, .1 / 152.38, .1 / 152.38)
    #glScale(.4, .5, 1)
    score1=str(score)
    string = score1.encode()  # conversion from Unicode string to byte string
    #print(string)
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)

def draw_level():
    global level
    glLoadIdentity()
    glLineWidth(5)  # Line with 3px
    glColor(1, 1, 1)  # white Color
    glLoadIdentity()
    glTranslate(.48, -.3, 0)
    glScale(.1 / 152.38, .1 / 152.38, .1 / 152.38)
    # glScale(.4, .5, 1)
    level1 = str(level)
    string1 = level1.encode()  # conversion from Unicode string to byte string
    # print(string)
    for c in string1:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)

def draw_goal():
    global goal
    glLoadIdentity()
    glLineWidth(4)  # Line with 3px
    glColor(1, 1, 1)  # white Color
    glLoadIdentity()
    glTranslate(.68, .1, 0)
    glScale(.1 / 152.38, .1 / 152.38, .1 / 152.38)
    goal1 = str(goal)
    string2 = goal1.encode()  # conversion from Unicode string to byte string
    # print(string)
    for c in string2:
     glutStrokeCharacter(GLUT_STROKE_ROMAN, c)

##################################################################################################################################





##################################################################################################################################

#shapes classing

# to define the square shape and it's bits in the matrix(floor)
class Square:
    def __init__(self,x=5,y=19):
        # each bit represents the position of one block of the whole shape
        self.bitone = [x, y]
        self.bittwo = [x+1, y]
        self.bitthree = [x+1, y+1]
        self.bitfour = [x, y+1]
        self.restore=[0,0,1,1]      # array storing the added value to vertical position to use it in resetduplicatepos ()


         # each bit represents the position of one block of the whole shape
        """
        the rotations bits
        down:1,2,3,4
        right:5,2,3,4
        left:1,2,4,5
        up:1,2,3,5
        """
        self.bitone = [x, y]
        self.bittwo = [x+1, y]
        self.bitthree = [x+1, y+1]
        self.bitfour = [x, y+1]
        self.bitfive= [x,y]
        self.bitsix= [x,y]
        self.bitseven= [x,y]
        self.biteight=[x, y]
        self.restore1=[0,0,1,1]
        self.restore2=[0,0,1,1]
        self.restore3=[0,0,1,1] 
        self.restore4=[0,0,1,1] 

        self.used1=self.bitone
        self.used2=self.bittwo
        self.used3=self.bitthree
        self.used4=self.bitfour
        self.restore=self.restore1   # array storing the added value to vertical position to use it in resetduplicatepos ()


        self.info = 'S'

# to define the I shape and it's bits in the matrix(floor)
class Iblock:
    def __init__(self,x=5,y=19):
       # each bit represents the position of one block of the whole shape
        """
        the rotations bits
        vertical:1,2,3,4
        horizontal:3,5,6,7
        """

        #all possibilities of blocks


        self.bitone = [x, y]
        self.bittwo = [x, y+1]
        self.bitthree = [x, y+2]
        self.bitfour = [x, y+3]
        self.bitfive=[x-1,y+2]
        self.bitsix=[x-2,y+2]
        self.bitseven=[x-3,y+2]
        self.biteight=[x, y]

        #the possible arrays to restore initial position
        self.restore1=[0,1,2,3]
        self.restore2=[2,2,2,2] 

        #the used blocks
        self.used1=self.bitone
        self.used2=self.bittwo
        self.used3=self.bitthree
        self.used4=self.bitfour


        self.restore=[0,1,2,3]      # array storing the added value to vertical position to use it in resetduplicatepos ()

        self.info = 'I'

# to define the L shape and it's bits in the matrix(floor)
class Lblock:
    def __init__(self,x=5,y=19):
        # each bit represents the position of one block of the whole shape
        """
        the rotations bits
        1:1,2,3,4
        2:5,4,1,6
        3:3.2.1.8
        4:5,3,7,6
        """
        #all possibilities of blocks
        self.bitone = [x, y]
        self.bittwo = [x, y+2]
        self.bitthree = [x, y+1]
        self.bitfour = [x+1, y]
        self.bitfive= [x+1,y+1]
        self.bitsix= [x-1,y]
        self.bitseven= [x-1,y+1]
        self.biteight=[x-1, y+2]

        #the possible arrays to restore initial position
        self.restore1=[0,2,1,0] 
        self.restore2=[1,0,0,0]
        self.restore3=[0,1,2,2]
        self.restore4=[1,1,1,0]

        #used blocks
        self.used1=self.bitone
        self.used2=self.bittwo
        self.used3=self.bitthree
        self.used4=self.bitfour
        self.restore=self.restore1   # array storing the added value to vertical position to use it in resetduplicatepos ()


        self.info = 'L'

# to define the T shape and it's bits in the matrix(floor)
class Tblock:
    def __init__(self,x=5,y=19):

        
        """
        the rotations bits
        down:1,2,3,4
        right:5,2,3,4
        left:1,2,4,5
        up:1,2,3,5
        """

        #all possibilities of blocks
        self.bitone = [x, y]
        self.bittwo = [x+1, y]
        self.bitthree = [x+2, y]
        self.bitfour = [x+1, y-1]
        self.bitfive= [x+1,y+1]
        self.bitsix= [x+1,y+1]
        self.bitseven= [x,y]
        self.biteight=[x, y]

        #the possible arrays to restore initial position
        self.restore1=[0,0,0,-1]
        self.restore2=[1,0,0,-1] 
        self.restore3=[0,0,0,1] 
        self.restore4=[0,0,-1,1]  
        self.info = 'T'

        #used blocks
        self.used1=self.bitone
        self.used2=self.bittwo
        self.used3=self.bitthree
        self.used4=self.bitfour
        self.restore=self.restore1   # array storing the added value to vertical position to use it in resetduplicatepos ()

# to define the N shape and it's bits in the matrix(floor)
class Nblock:
    def __init__(self,x=5,y=19):
        # each bit represents the position of one block of the whole shape
        """
        the rotations bits
        z:1,2,3,4
        n:5,6,3,4
        """

        #all possibilities of blocks
        self.bitone = [x , y]
        self.bittwo = [x+1, y]
        self.bitthree = [x+1, y+1]
        self.bitfour = [x+2, y+1]
        self.bitfive = [x+2 , y]
        self.bitsix=[x+1, y+2]
        self.bitseven= [x,y]
        self.biteight=[x, y]

        #the possible arrays to restore initial position
        self.restore1=[0,0,1,1]
        self.restore2=[0,2,1,1] 

        #the used blocks
        self.used1=self.bitone
        self.used2=self.bittwo
        self.used3=self.bitthree
        self.used4=self.bitfour
        self.restore=self.restore1   # array storing the added value to vertical position to use it in resetduplicatepos ()


        self.info = 'N'
################################################################################################################################################################





################################################################################################################################################################
#duplicate functions
def duplicateposition():
    global floor
    global duplicate
    # if it has reaching the ground or it's about to overlap another shape
    if (floor[duplicate.used4[1] - 1][duplicate.used4[0]] == 1
            or floor[duplicate.used3[1] - 1][duplicate.used3[0]] == 1
            or floor[duplicate.used2[1] - 1][duplicate.used2[0]] == 1
            or floor[duplicate.used1[1] - 1][duplicate.used1[0]] == 1
            or duplicate.used4[1] <= 0
            or duplicate.used3[1] <= 0
            or duplicate.used2[1] <= 0
            or duplicate.used1[1] <= 0):
        return True
    else:
        # shift bits shift the shape
        duplicate.biteight[1] -= 1
        duplicate.bitseven[1] -= 1
        duplicate.bitsix[1] -= 1
        duplicate.bitfive[1] -= 1
        duplicate.bitfour[1] -= 1
        duplicate.bitthree[1] -= 1
        duplicate.bittwo[1] -= 1
        duplicate.bitone[1] -= 1

        duplicateposition()

def resetduplicatepos ():  #reset the position of duplicate to be calculted right(must be called before duplicateposition())
    global duplicate
    global currentshape
    duplicate.used1[1] = 19+duplicate.restore[0]
    duplicate.used2[1] = 19+duplicate.restore[1]
    duplicate.used3[1] = 19+duplicate.restore[2]
    duplicate.used4[1] = 19+duplicate.restore[3]

    duplicate.used1[0] = currentshape.used1[0]
    duplicate.used2[0] = currentshape.used2[0]
    duplicate.used3[0] = currentshape.used3[0]
    duplicate.used4[0] = currentshape.used4[0]

# to draw the shape according to its class each shape is four blocks
def drawduplicate():
    global duplicate
    global texture

    resetduplicatepos()
    duplicateposition()

    
    glBegin(GL_QUADS)
    glColor(1, 1, 1,1)
    # first block
    glVertex(awidth[duplicate.used1[0] + 1], aheight[duplicate.used1[1]])
    glVertex(awidth[duplicate.used1[0]],     aheight[duplicate.used1[1]])
    glVertex(awidth[duplicate.used1[0]],     aheight[duplicate.used1[1] + 1])
    glVertex(awidth[duplicate.used1[0] + 1], aheight[duplicate.used1[1] + 1])

    # second block
    glVertex(awidth[duplicate.used2[0] + 1], aheight[duplicate.used2[1]])
    glVertex(awidth[duplicate.used2[0]],     aheight[duplicate.used2[1]])
    glVertex(awidth[duplicate.used2[0]],     aheight[duplicate.used2[1] + 1])
    glVertex(awidth[duplicate.used2[0] + 1], aheight[duplicate.used2[1] + 1])

    # third block
    glVertex(awidth[duplicate.used3[0] + 1], aheight[duplicate.used3[1]])
    glVertex(awidth[duplicate.used3[0]],     aheight[duplicate.used3[1]])
    glVertex(awidth[duplicate.used3[0]],     aheight[duplicate.used3[1] + 1])
    glVertex(awidth[duplicate.used3[0] + 1], aheight[duplicate.used3[1] + 1])

    # fourth block
    glVertex(awidth[duplicate.used4[0] + 1], aheight[duplicate.used4[1]])
    glVertex(awidth[duplicate.used4[0]],     aheight[duplicate.used4[1]])
    glVertex(awidth[duplicate.used4[0]],     aheight[duplicate.used4[1] + 1])
    glVertex(awidth[duplicate.used4[0] + 1], aheight[duplicate.used4[1] + 1])

    glColor(1,1,1)

    glEnd()
################################################################################################################################################################




################################################################################################################################################################
#pick shape and draw

# initialize the type of variable currentshape
currentshape = Square()
duplicate = Square() # the other blurry shape the indicates the finial position
nextshape=Nblock(11,10)

# to create a new random shape
def nextShape():
    global nextshape
    global x
    x=x+1
    n=random.randint(1, 5)
    x = x%6+1

    glLoadIdentity()
    if n == 1:
        nextshape = Square(13,10)
        return

    elif n == 2:
        nextshape = Tblock(12,11)
        return

    elif n == 3:
        nextshape = Nblock(11,10)
        return

    elif n == 4:
        nextshape = Lblock(12,10)
        return

    elif n == 5:
        nextshape = Iblock(13,10)
        return

# to create a new random shape
def pickCurrent():
    global currentshape
    global duplicate
    glLoadIdentity()
    if nextshape.info=='S':
        duplicate = Square()
        currentshape = Square()
        return

    elif nextshape.info=='T':
        duplicate = Tblock()
        currentshape = Tblock()
        return

    elif nextshape.info=='N':
        duplicate = Nblock()
        currentshape = Nblock()
        return

    elif nextshape.info=='L':
        duplicate = Lblock()
        currentshape = Lblock()
        return

    elif nextshape.info=='I':
        duplicate = Iblock()
        currentshape = Iblock()
        return

# to draw the shape according to its class each shape is four blocks
def drawshapes(currentshape2):
    global currentshape
    global duplicate
    global texture
    global cnt
    global x  # the color of the shape

    #to make sure shapes are inside boundaries
    while (currentshape.used1[0] < 0
            or currentshape.used2[0] < 0
            or currentshape.used3[0] < 0
            or currentshape.used4[0] < 0):

            # shift bits to shift the shape
            currentshape.biteight[0] += 1
            currentshape.bitseven[0] += 1
            currentshape.bitsix[0] += 1
            currentshape.bitfive[0] += 1
            currentshape.bitfour[0] += 1
            currentshape.bitthree[0] += 1
            currentshape.bittwo[0] += 1
            currentshape.bitone[0] += 1



    while (currentshape.used1[0] >= 10
            or currentshape.used2[0] >= 10
            or currentshape.used3[0] >= 10
            or currentshape.used4[0] >= 10):

            # shift bits to shift the shape
            currentshape.biteight[0] -= 1
            currentshape.bitseven[0] -= 1
            currentshape.bitsix[0] -= 1
            currentshape.bitfive[0] -= 1
            currentshape.bitfour[0] -= 1
            currentshape.bitthree[0] -= 1
            currentshape.bittwo[0] -= 1
            currentshape.bitone[0] -= 1


    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture[x])
    glBegin(GL_QUADS)

    if (currentshape2.used1[1] + 1 <= 20):
        # first block
        glTexCoord(0, 0)
        glVertex(awidth[currentshape2.used1[0]], aheight[currentshape2.used1[1]])
        glTexCoord(0, 1)
        glVertex(awidth[currentshape2.used1[0] + 1], aheight[currentshape2.used1[1]])
        glTexCoord(1, 1)
        glVertex(awidth[currentshape2.used1[0] + 1], aheight[currentshape2.used1[1]+1])
        glTexCoord(1, 0)
        glVertex(awidth[currentshape2.used1[0]], aheight[currentshape2.used1[1] + 1])

    if (currentshape2.used2[1] + 1 <= 20):
        # second block
        glTexCoord(0, 0)
        glVertex(awidth[currentshape2.used2[0]], aheight[currentshape2.used2[1]])
        glTexCoord(0, 1)
        glVertex(awidth[currentshape2.used2[0] + 1], aheight[currentshape2.used2[1]])
        glTexCoord(1, 1)
        glVertex(awidth[currentshape2.used2[0] + 1], aheight[currentshape2.used2[1]+1])
        glTexCoord(1, 0)
        glVertex(awidth[currentshape2.used2[0]], aheight[currentshape2.used2[1] + 1])

    if (currentshape2.used3[1]+1 <= 20):
        # third block
        glTexCoord(0, 0)
        glVertex(awidth[currentshape2.used3[0]], aheight[currentshape2.used3[1]])
        glTexCoord(0, 1)
        glVertex(awidth[currentshape2.used3[0] + 1], aheight[currentshape2.used3[1]])
        glTexCoord(1, 1)
        glVertex(awidth[currentshape2.used3[0] + 1], aheight[currentshape2.used3[1]+1])
        glTexCoord(1, 0)
        glVertex(awidth[currentshape2.used3[0]], aheight[currentshape2.used3[1] + 1])

    if (currentshape2.used4[1]+1 <= 20):
        # fourth block
        glTexCoord(0, 0)
        glVertex(awidth[currentshape2.used4[0]], aheight[currentshape2.used4[1]])
        glTexCoord(0, 1)
        glVertex(awidth[currentshape2.used4[0] + 1], aheight[currentshape2.used4[1]])
        glTexCoord(1, 1)
        glVertex(awidth[currentshape2.used4[0] + 1], aheight[currentshape2.used4[1]+1])
        glTexCoord(1, 0)
        glVertex(awidth[currentshape2.used4[0]], aheight[currentshape2.used4[1] + 1])

    glEnd()

    
################################################################################################################################################################





################################################################################################################################################################
#moving

# move right and left
def movement():
    # print("ll")
    global deltap
    global deltan
    global currentshape
    global duplicate

    # move right
    if deltap == 1:
        # make sure there is no neighbouring block and the block hasn't reached the right wall
        if (currentshape.used1[0] <= 8
            and currentshape.used2[0] <= 8
            and currentshape.used3[0] <= 8
            and currentshape.used4[0] <= 8
            and floor[currentshape.used4[1]][currentshape.used4[0] + 1] != 1
            and floor[currentshape.used3[1]][currentshape.used3[0] + 1] != 1
            and floor[currentshape.used2[1]][currentshape.used2[0] + 1] != 1
            and floor[currentshape.used1[1]][currentshape.used1[0] + 1] != 1):
            # shift bits to shift the shape
            currentshape.biteight[0] += 1
            currentshape.bitseven[0] += 1
            currentshape.bitsix[0] += 1
            currentshape.bitfive[0] += 1
            currentshape.bitfour[0] += 1
            currentshape.bitthree[0] += 1
            currentshape.bittwo[0] += 1
            currentshape.bitone[0] += 1


        # reset back to zero to shift only one bit per second
        deltap = 0

    # move left
    if deltan == 1:
        # make sure there is no neighbouring shape and the block hasn't reached the left wall
        if (currentshape.used1[0] >= 1
                and currentshape.used2[0] >= 1
                and currentshape.used3[0] >= 1
                and currentshape.used4[0] >= 1
                and floor[currentshape.used1[1]][currentshape.used1[0] - 1] != 1
                and floor[currentshape.used2[1]][currentshape.used2[0] - 1] != 1
                and floor[currentshape.used3[1]][currentshape.used3[0] - 1] != 1
                and floor[currentshape.used4[1]][currentshape.used4[0] - 1] != 1):

            # shift bits to shift the shape
            currentshape.biteight[0]-=1
            currentshape.bitseven[0]-=1
            currentshape.bitsix[0] -= 1      
            currentshape.bitfive[0] -= 1
            currentshape.bitfour[0] -= 1
            currentshape.bitthree[0] -= 1
            currentshape.bittwo[0] -= 1
            currentshape.bitone[0] -= 1

        # reset back to zero to shift only one bit per second
        deltan = 0

# to move down one bit per second
def automove():
    # check if the shape should stop before
    #  making a move
    stopped()

    # shift bits shift the shape
    currentshape.biteight[1]-=1
    currentshape.bitseven[1]-=1
    currentshape.bitsix[1]-=1
    currentshape.bitfive[1]-=1
    currentshape.bitfour[1]-=1
    currentshape.bitthree[1]-=1
    currentshape.bittwo[1]-=1
    currentshape.bitone[1]-=1

def Rotate():
    global currentshape
    global rotate

    if(currentshape.info=='T'):
        #position 1
        if(rotate%4==0):
            currentshape.used1=currentshape.bitone
            currentshape.used2=currentshape.bittwo
            currentshape.used3=currentshape.bitthree
            currentshape.used4=currentshape.bitfour

             #set restore array to be able to restore vertical position
            duplicate.restore=duplicate.restore1

        #position 2
        elif(rotate%4==1):
            currentshape.used1=currentshape.bitfive
            currentshape.used2=currentshape.bittwo
            currentshape.used3=currentshape.bitthree
            currentshape.used4=currentshape.bitfour

             #set restore array to be able to restore vertical position
            duplicate.restore=duplicate.restore2


        #position 3
        elif(rotate%4==2):
            currentshape.used1=currentshape.bitone
            currentshape.used2=currentshape.bittwo
            currentshape.used3=currentshape.bitthree
            currentshape.used4=currentshape.bitfive

             #set restore array to be able to restore vertical position
            duplicate.restore=duplicate.restore3

        #position 4
        else:
            currentshape.used1=currentshape.bitone
            currentshape.used2=currentshape.bittwo
            currentshape.used3=currentshape.bitfour
            currentshape.used4=currentshape.bitfive

             #set restore array to be able to restore vertical position
            duplicate.restore=duplicate.restore4



    elif(currentshape.info=='N'):
        #position 1
        if(rotate%2==0):
            currentshape.used1=currentshape.bitone
            currentshape.used2=currentshape.bittwo
            currentshape.used3=currentshape.bitthree
            currentshape.used4=currentshape.bitfour

             #set restore array to be able to restore vertical position
            duplicate.restore=duplicate.restore1

        #position 2
        else:
            currentshape.used1=currentshape.bitfive
            currentshape.used2=currentshape.bitsix
            currentshape.used3=currentshape.bitthree
            currentshape.used4=currentshape.bitfour

             #set restore array to be able to restore vertical position
            duplicate.restore=duplicate.restore2

    elif(currentshape.info=='L'):

        #position 1
        if(rotate%4==0):
            currentshape.used1=currentshape.bitone
            currentshape.used2=currentshape.bittwo
            currentshape.used3=currentshape.bitthree
            currentshape.used4=currentshape.bitfour

             #set restore array to be able to restore vertical position
            duplicate.restore=duplicate.restore1

        #position 2
        elif(rotate%4==1):
            currentshape.used1=currentshape.bitfive
            currentshape.used2=currentshape.bitfour
            currentshape.used3=currentshape.bitone
            currentshape.used4=currentshape.bitsix

             #set restore array to be able to restore vertical position
            duplicate.restore=duplicate.restore2


        #position 3
        elif(rotate%4==2):
            currentshape.used1=currentshape.bitthree
            currentshape.used2=currentshape.bittwo
            currentshape.used3=currentshape.bitone
            currentshape.used4=currentshape.biteight

             #set restore array to be able to restore vertical position
            duplicate.restore=duplicate.restore3

        #position 4
        else:
            currentshape.used1=currentshape.bitfive
            currentshape.used2=currentshape.bitthree
            currentshape.used3=currentshape.bitseven
            currentshape.used4=currentshape.bitsix

             #set restore array to be able to restore vertical position
            duplicate.restore=duplicate.restore4

    
    elif(currentshape.info=='I'):
        #position 1
        if(rotate%2==0):
            currentshape.used1=currentshape.bitone
            currentshape.used2=currentshape.bittwo
            currentshape.used3=currentshape.bitthree
            currentshape.used4=currentshape.bitfour

             #set restore array to be able to restore vertical position
            duplicate.restore=duplicate.restore1

        #position 2
        else:
            currentshape.used1=currentshape.bitthree
            currentshape.used2=currentshape.bitfive
            currentshape.used3=currentshape.bitsix
            currentshape.used4=currentshape.bitseven

             #set restore array to be able to restore vertical position
            duplicate.restore=duplicate.restore2



    resetduplicatepos()
    duplicateposition()
################################################################################################################################################################





################################################################################################################################################################
#control
def keyPressed(key, x, y):
    # delap for moving right deltan for moving left s for moving down and r for rotating
    global deltap
    global deltan
    global duplicate
    global currentshape
    global rotate
    global control_sound
    global start_background
    if key == b'q':
        sys.exit()
    elif key ==b'g':
        start_background=0

    elif key == b'a':
        deltan = 1
        deltap = 0

    elif key == b'd':
        deltap = 1
        deltan = 0

    elif key == b's':
        currentshape = duplicate
        solid(duplicate)

    elif key==b'r':
        rotate+=1
        Rotate()

    #sound control
    elif key ==b'x':
        control_sound= not control_sound
        if control_sound:
            soundSrc[0].play()

        else:
            soundSrc[0].stop()
            soundSrc[1].stop()
            soundSrc[2].stop()
            soundSrc[3].stop()

    else:
        deltap = 0
        deltan = 0
################################################################################################################################################################


################################################################################################################################################################
#stop and recreate

# to check if the shape should stop moving and create another shape
def istouching():
    global floor
    # if it has reaching the ground or it's about to overlap another shape
    if (floor[currentshape.used1[1] - 1][currentshape.used1[0]] == 1
            or floor[currentshape.used2[1] - 1][currentshape.used2[0]] == 1
            or floor[currentshape.used3[1] - 1][currentshape.used3[0]] == 1
            or floor[currentshape.used4[1] - 1][currentshape.used4[0]] == 1
            or currentshape.used1[1] <= 0
            or currentshape.used2[1] <= 0
            or currentshape.used3[1] <= 0
            or currentshape.used4[1] <= 0):
        return True
    else:
        return False


# if the shape has stopped it's position and color must be saved to be drawn every scene
def solid(currentshape):
    global x

    # the position of the shape
    floor[currentshape.used4[1]][currentshape.used4[0]] = 1
    floor[currentshape.used3[1]][currentshape.used3[0]] = 1
    floor[currentshape.used2[1]][currentshape.used2[0]] = 1
    floor[currentshape.used1[1]][currentshape.used1[0]] = 1

    # the color of the shape
    color[currentshape.used4[1]][currentshape.used4[0]] = x
    color[currentshape.used3[1]][currentshape.used3[0]] = x
    color[currentshape.used2[1]][currentshape.used2[0]] = x
    color[currentshape.used1[1]][currentshape.used1[0]] = x


# to check if the shape should stop then it'd create another random shape
def stopped():
    global floor
    global currentshape
    global control_sound
    global score
    # if it should stop save it's position and color,check if there is a full line to be deleted and create a new shape
    if (istouching()):
        solid(currentshape)
        score += 10
        #print(score)
        if control_sound:
         soundSrc[2].play()

        fullline()
        pickCurrent()
        nextShape()

################################################################################################################################################################



################################################################################################################################################################

#the floor matrix

# to draw the shapes that has stopped earlier (block by block)
def drawfloor():

    for i in range(0, 22):
        for j in range(0, 10):
            if (floor[i][j] == 1):
                glEnable(GL_TEXTURE_2D)
                glBindTexture(GL_TEXTURE_2D,
                              texture[color[i][j]])  # using the color saved in the color matrix using function solid()
                glBegin(GL_QUADS)
                glTexCoord(0, 0)
                glVertex(awidth[j], aheight[i])
                glTexCoord(0, 1)
                glVertex(awidth[j + 1], aheight[i])
                glTexCoord(1, 1)
                glVertex(awidth[j + 1], aheight[i + 1])
                glTexCoord(1, 0)
                glVertex(awidth[j], aheight[i + 1])
                glEnd()
                glDisable(GL_TEXTURE_2D)

# to return the index of the full line
def loop():
    for i in range(0, 22):
        if (floor[i] == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]):
            return i
    return -1
# sound flaf
winny=0
def win():
    global score
    global goal
    global winny
    if winny ==0:
      if score >= goal :
        draw_win()
        soundSrc[0].stop()
        soundSrc[4].play()
        winny=1
    else:
        draw_win()
        soundSrc[0].stop()
        soundSrc[1].stop()
        soundSrc[2].stop()
        soundSrc[3].stop()
        soundSrc[4].stop()


        

# check if there is a new line to be deleted
def fullline():
    global score
    position = loop()

    if (position != -1):
        for j in range(position, 19):
            floor[j] = floor[j + 1]
        floor[19] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # add a new empty line at the top
        score+=100
        fullline()  # check again for full line because of shifting

r=0 # flag for gameover no to declare gameover from the start round
gamme=0 #flag for gameover sound
# check if the player lost
def gameover():
    global floor
    global color
    global gameoverrt
    global level_time_sec
    global   r
    global gamme
    r+=1

    if ((floor[19] != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) and (r>2) ) or level_time_sec <= 0 :
        # reset the game to beginning state
        gameoverrt = 3
    
        
    if  gamme==0:
      if gameoverrt==3:
        draw_gameover()
        soundSrc[1].play()
        soundSrc[0].stop()
        gameoverrt = 0
        gamme=1
    else:
        draw_gameover()
        soundSrc[0].stop()
        soundSrc[1].stop()
        soundSrc[2].stop()
        soundSrc[3].stop()
        soundSrc[4].stop()

        

################################################################################################################################################################



################################################################################################################################################################
#Main

def Display():
    global time_interval
    global frame_count
    global score
    global start_background
    global gameoverrt
    if start_background:
        draw_start()
        glutSwapBuffers()
    else:
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     glLoadIdentity()

     draw_background()

     glPushMatrix()
     level_time()
     glLoadIdentity()
     draw_level()
     glLoadIdentity()
     draw_goal()
     glPopMatrix()

     movement()
     stopped()
     drawfloor()

     glLoadIdentity()

     drawshapes(currentshape)
     drawshapes(nextshape)
     drawduplicate()
     glLoadIdentity()

     draw_score()
     glLoadIdentity()
    # glDeleteTextures(5, texture)
     automove()
     win()
     gameover()
     glutSwapBuffers()


# The Main Display Declareation
def main():
    global FPS
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowPosition(100, 50)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Tetris Blocks")
    glutDisplayFunc(Display)
    glutKeyboardFunc(keyPressed)
    glutTimerFunc(time_interval, timer, 1)
    init()
    glutMainLoop()


# The Main Call
main()