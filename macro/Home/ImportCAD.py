import JPT
from macro_defs import *
from macroTypes import *

def Elysium(strlPaths, dChordHeightTolerance=1.0, dAngleToleranceDegree=5.0, dPointCoincidentTolerance=0.01, iConvertIsolatedCurve=0, iDekCleanselfintersectingloop=2, iDekVolumetopart=4, iIgesFixedcurevepreference=0, iIgesAutostitch=1, dIgesStitchtolerance=0.1, iCatiaConvertNotShownElement=0, iCatiaConvertNotShownInstance=0, iCatiaConvertaxis=1, iStepCreateseam=1, dStepPointtolerance=0.0, iAcisHealacisbeforeversion=0, iJtConvertgeometrytype=2, bFaceColor=False, iJtConvertgeneralpart=1, iJtConvertaxis=1, iJtConvertcenterline=0):
    bFaceColor_b = 1 if bFaceColor else 0
    strCmd = 'ImportElysium({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20})'.format(
        '[' + ', '.join('"' + tok + '"' for tok in strlPaths) + ']',
        dChordHeightTolerance,
        dAngleToleranceDegree,
        iConvertIsolatedCurve,
        iIgesFixedcurevepreference,
        iIgesAutostitch,
        dIgesStitchtolerance,
        iCatiaConvertNotShownElement,
        iCatiaConvertNotShownInstance,
        iCatiaConvertaxis,
        iStepCreateseam,
        dStepPointtolerance,
        iAcisHealacisbeforeversion,
        iJtConvertgeometrytype,
        iJtConvertgeneralpart,
        iJtConvertaxis,
        iJtConvertcenterline,
        bFaceColor_b,
        iDekCleanselfintersectingloop,
        dPointCoincidentTolerance,
        iDekVolumetopart)
    return getBoolValueFromString(JPT.Exec(strCmd))

def Spatial(strlPaths, dSurfacePlaneTolerance=0.0, dSurfacePlaneAngle=20.0, dMaxFacetWidth=100.0, bNXMultipart=True, bHealing=True, bSetFaceColor=False):
    dMaxFacetWidth = JPT.ConvertFromMacroUnit(dMaxFacetWidth, JPT.UnitType.Unit_Length, "mm")
    NX_multibody_b = 1 if bNXMultipart else 0
    healing_b = 1 if bHealing else 0
    isNXDirect_b = 0
    setFaceColor_b = 1 if bSetFaceColor else 0
    strCmd = 'ImportSpatial({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})'.format(
        '[' + ', '.join('"' + tok + '"' for tok in strlPaths) + ']',
        dSurfacePlaneTolerance,
        dSurfacePlaneAngle,
        dMaxFacetWidth,
        NX_multibody_b,
        healing_b,
        isNXDirect_b,
        setFaceColor_b,
        '""')
    return getBoolValueFromString(JPT.Exec(strCmd))

def Parasolid(strlPaths, dChordHeightTolerance=0.0, dAngleToleranceDegree=7.0, dSurfacePlaneTolerance=0.0, dSurfacePlaneAngle=20.0, dMaxFacetWidth=0.1, dMinFacetWidth=0.0, dScale=1.0, bUseColorInformation=False):
    bUseColorInformation_b = 1 if bUseColorInformation else 0
    strCmd = 'ImportDirect_Parasolid({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9})'.format(
        '[' + ', '.join('"' + tok + '"' for tok in strlPaths) + ']',
        dChordHeightTolerance,
        dAngleToleranceDegree,
        0,
        dSurfacePlaneTolerance,
        dSurfacePlaneAngle,
        dMaxFacetWidth,
        dMinFacetWidth,
        dScale,
        bUseColorInformation_b)
    return getBoolValueFromString(JPT.Exec(strCmd))

def STL(strlPaths, dScale=0.001):
    strCmd = 'ImportDirect_STL({0}, {1})'.format(
        '[' + ', '.join('"' + tok + '"' for tok in strlPaths) + ']',
        dScale)
    return getBoolValueFromString(JPT.Exec(strCmd))

def VRML(strlPaths, iVRMLColorGroups=0, dScale=1.0):
    strCmd = 'ImportDirect_VRML({0}, {1}, {2})'.format(
        '[' + ', '.join('"' + tok + '"' for tok in strlPaths) + ']',
        iVRMLColorGroups,
        dScale)
    return getBoolValueFromString(JPT.Exec(strCmd))

def ProECreoDirect(strlPaths, dChordHeightTolerance=0.0, dAngleToleranceDegree=20.0, dStepMaxSize=0.1):
    strCmd = 'ImportCreo({0}, {1}, {2}, {3})'.format(
        '[' + ', '.join('"' + tok + '"' for tok in strlPaths) + ']',
        dChordHeightTolerance,
        dAngleToleranceDegree,
        dStepMaxSize)
    return getBoolValueFromString(JPT.Exec(strCmd))

def GeomBDF(strlPaths, bUseUnit=True):
    use_unit_b = 1 if bUseUnit else 0
    strCmd = 'ImportGeomBDF({0}, {1})'.format(
        '[' + ', '.join('"' + tok + '"' for tok in strlPaths) + ']',
        use_unit_b)
    return JPT.Exec(strCmd)

def TechnoStarGeometry(strlPaths, bUseUnit=True):
    use_unit_b = 1 if bUseUnit else 0
    strCmd = 'ImportTSG({0}, {1})'.format(
        '[' + ', '.join('"' + tok + '"' for tok in strlPaths) + ']',
        use_unit_b)
    return JPT.Exec(strCmd)