from jupiterutils.Utility import JPT
from jupiterutils.macro_defs import *

# Base class


class MESH_QUALITY:
    def __init__(
            self,
    ):
        ...

    def from_list(
            self,
            list: list,
    ):
        return self
        ...

    def from_str(
            self,
            str: str,
    ):
        return self
        ...

# Derived classes


class MESH_QUALITY_FREE_EDGE(MESH_QUALITY):
    def __init__(
        self,
        bSuccess=True,
        iFreeEdges=0,
        crlElemEdges=[],
        iNonManifoldEdges=0,
        crlNonManifoldEdges=[],
    ):
        self.bSuccess = bSuccess
        self.iFreeEdges = iFreeEdges
        self.crlElemEdges = crlElemEdges
        self.iNonManifoldEdges = iNonManifoldEdges
        self.crlNonManifoldEdges = crlNonManifoldEdges

    def from_list(self, list: str):
        if len(list) > 0:
            self.bSuccess = list[0]
        if len(list) > 1:
            self.iFreeEdges = list[1]
        if len(list) > 2:
            self.crlElemEdges.clear()
            for item in list[2]:
                cursor_data = item.getCursorData()
                self.crlElemEdges.append(cursor_data)
        if len(list) > 3:
            self.iNonManifoldEdges = list[3]
        if len(list) > 4:
            self.crlNonManifoldEdges.clear()
            for item in list[4]:
                cursor_data = item.getCursorData()
                self.crlNonManifoldEdges.append(cursor_data)
        return self

    def from_str(self, str: str):
        listParam = []
        if str is not None:
            listStr = custom_split(str, ", ")
            if listStr is not []:
                bNoFreeEdgeData = False
                if len(listStr) > 0:
                    listParam.append(int(listStr[0]))
                if len(listStr) > 1:
                    iFreeEdges = int(listStr[1])
                    listParam.append(iFreeEdges)
                    if iFreeEdges == 0:
                        bNoFreeEdgeData = True
                if len(listStr) > 2:
                    if int(listStr[1]) > 0:
                        listParam.append(getListCursorPairFromStr(listStr[2]))
                    else:
                        listParam.append([])
                if len(listStr) > 3:
                    if bNoFreeEdgeData:
                        listParam.append(int(listStr[2]))
                    else:
                        listParam.append(int(listStr[3]))
                if len(listStr) > 4:
                    if bNoFreeEdgeData:
                        if int(listStr[2]) > 0:
                            listParam.append(
                                getListCursorPairFromStr(listStr[3]))
                        else:
                            listParam.append([])
                    else:
                        if int(listStr[3]) > 0:
                            listParam.append(
                                getListCursorPairFromStr(listStr[4]))
                        else:
                            listParam.append([])
                return self.from_list(listParam)
        return self

    def __str__(self):
        return_str = ''
        return_str += f"bSuccess = {self.bSuccess}\n"
        return_str += f">> iFreeEdges = {self.iFreeEdges}\n"
        return_str += f">> crlElemEdges (count) = {self.iFreeEdges}\n"
        return_str += f">> iNonManifoldEdges = {self.iNonManifoldEdges}\n"
        return_str += f">> crlNonManifoldEdges (count) = {self.iNonManifoldEdges}\n"
        return return_str


class MESH_QUALITY_INTERSECTION(MESH_QUALITY):
    def __init__(
        self,
        bSuccess=True,
        iIntersectElements=0,
        crlElemEdges=[],
    ):
        self.bSuccess = bSuccess
        self.iIntersectElements = iIntersectElements
        self.crlElemEdges = crlElemEdges

    def from_list(self, list: str):
        if len(list) > 0:
            self.bSuccess = list[0]
        if len(list) > 1:
            self.iIntersectElements = list[1]
        if len(list) > 2:
            self.crlElemEdges.clear()
            for item in list[2]:
                cursor_data = item.getCursorData()
                self.crlElemEdges.append(cursor_data)
        return self

    def from_str(self, str: str):
        listParam = []
        if str is not None:
            listStr = custom_split(str, ", ")
            if listStr is not []:
                if len(listStr) > 0:
                    listParam.append(getBoolValue(int(listStr[0])))
                if len(listStr) > 1:
                    listParam.append(int(listStr[1]))
                if len(listStr) > 2:
                    listParam.append(getListCursorFromStr(listStr[2]))
                return self.from_list(listParam)
        return self

    def __str__(self):
        return_str = ''
        return_str += f"bSuccess = {self.bSuccess}\n"
        return_str += f">> iIntersectElements = {self.iIntersectElements}\n"
        return_str += f">> crlElemEdges (count) = {self.iIntersectElements}\n"
        return return_str
