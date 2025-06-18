from constants import *
import math

class Mat4x4:
    fNear = 0.1
    fFar = 1000
    fFOV = 90
    fAspectRatio = SCREEN_HEIGHT / SCREEN_WIDTH
    fFOVRad = 1/math.tan(fFOV * 0.5 / 180*math.pi)
    projmat =  [[fAspectRatio*fFOVRad,0,0,0],
                [0,fFOVRad,0,0],
                [0,0, fFar/(fFar-fNear), 1],
                [0,0,(-fFar*fNear)/(fFar-fNear),0]]