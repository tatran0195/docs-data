from jupiterutils.Utility import JPT
from jupiterutils.macro_defs import *
from jupiterutils.macroTypes import *

def CopyMeshPattern(taSourceFace=[], taSourceNode=[], taTargetFace=[], taTargetNode=[]):
    strCmd = 'CopyMeshPattern({0}, {1}, {2}, {3})'.format(
        str(taSourceFace) if taSourceFace != [None] else '[0:0]',
        str(taSourceNode) if taSourceNode != [None] else '[0:0]',
        str(taTargetFace) if taTargetFace != [None] else '[0:0]',
        str(taTargetNode) if taTargetNode != [None] else '[0:0]')
    return JPT.Exec(strCmd)
