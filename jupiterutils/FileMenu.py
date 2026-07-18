from jupiterutils.Utility import JPT
from jupiterutils.macro_defs import *
from jupiterutils.macroTypes import *

def AddJTDB(strFileName, strMethod="AUTO", strTargetModel="IMPORTED", strOption="OFFSET", iInputNode=0, iInputElem=0, iInputPart=0, iInputFace=0,iInputEdge=0,iInputMaterial=0, iInputProperty=0, iInputInst=0, strTargetUnit="CURRENT"):
    strCmd = 'AddJTDB({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12})'.format(
        '"' + strFileName + '"',
        '"' + strMethod + '"',
        '"' + strTargetModel + '"',
        '"' + strOption + '"',
        iInputNode,
        iInputElem,
        iInputPart,
        iInputFace,
        iInputEdge,
        iInputMaterial,
        iInputProperty,
        iInputInst,
        '"' + strTargetUnit + '"')
    return JPT.Exec(strCmd)

def LoadJTDB(strFileName="", bUseTmpTable=False):
    bUseTmpTable_b = 1 if bUseTmpTable else 0
    strCmd = 'LoadDB({0}, {1})'.format(
        '"' + strFileName + '"',
        bUseTmpTable_b)
    return JPT.Exec(strCmd)

def SaveJTDB(strFileName, strHistoryTree=""):
    strCmd = 'SaveDB({0}, {1})'.format(
        '"' + strFileName + '"',
        '"' + strHistoryTree + '"')
    return JPT.Exec(strCmd)

def SaveJTH5(strFileName=""):
    strCmd = 'SaveJTH5({0})'.format(
        '"' + strFileName + '"')
    return JPT.Exec(strCmd)

def LoadJTH5(strFileName="", bUseTmpTable=False):
    bUseTmpTable_b = 1 if bUseTmpTable else 0
    strCmd = 'LoadJTH5({0}, {1})'.format(
        '"' + strFileName + '"',
        bUseTmpTable_b)
    return JPT.Exec(strCmd)

def SavePOH5(strFileName="",iSaveOption=0):
    strCmd = 'SavePOH5({0}, {1})'.format(
        '"' + strFileName + '"',
        iSaveOption)
    return JPT.Exec(strCmd)

def LoadPOH5(strFileName="", bUseTmpTable=False):
    bUseTmpTable_b = 1 if bUseTmpTable else 0
    strCmd = 'LoadPOH5({0}, {1})'.format(
        '"' + strFileName + '"',
        bUseTmpTable_b)
    return JPT.Exec(strCmd)