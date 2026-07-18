import JPT
from macro_defs import *
from macroTypes import *

def ResetCenter():  
    strCmd = 'ViewControl_ResetCenter()'
    return getBoolValueFromString(JPT.Exec(strCmd))

def SetCenter(dlCenter):  
    strCmd = 'ViewControl_SetCenter({0})'.format(dlCenter)
    return getBoolValueFromString(JPT.Exec(strCmd))

def Rotate(dlAngle):  
    strCmd = 'ViewControl_Rotate({0})'.format(dlAngle)
    return getBoolValueFromString(JPT.Exec(strCmd))

def PanUp(dDistance):  
    strCmd = 'ViewControl_Pan_Up({0})'.format(dDistance)
    return getBoolValueFromString(JPT.Exec(strCmd))

def PanDown(dDistance):  
    strCmd = 'ViewControl_Pan_Down({0})'.format(dDistance)
    return getBoolValueFromString(JPT.Exec(strCmd))

def PanRight(dDistance):  
    strCmd = 'ViewControl_Pan_Right({0})'.format(dDistance)
    return getBoolValueFromString(JPT.Exec(strCmd))

def PanLeft(dDistance):  
    strCmd = 'ViewControl_Pan_Left({0})'.format(dDistance)
    return getBoolValueFromString(JPT.Exec(strCmd))

def ZoomIn(dZoom=1.2):  
    strCmd = 'ViewControl_Zoom_In({0})'.format(dZoom)
    return getBoolValueFromString(JPT.Exec(strCmd))

def ZoomOut(dZoom=0.833333):  
    strCmd = 'ViewControl_Zoom_Out({0})'.format(dZoom)
    return getBoolValueFromString(JPT.Exec(strCmd))

def FitToModel():
    strCmd = 'View Fit To Model()'
    return getBoolValueFromString(JPT.Exec(strCmd))