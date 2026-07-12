---
id: MeshCleanup-AutoCheck-Quad
title: MeshCleanup.AutoCheck.Quad()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Correct the surface mesh (QUAD4/QUAD8) by using multiple mesh quality standards 
---

## Description

Correct the surface mesh (QUAD4/QUAD8) by using multiple mesh quality standards.

## Syntax

```psj
MeshCleanup.AutoCheck.Quad(...)
```

Macro:

Ribbon: <menuselection>MeshCleanup &#187; AutoCheck &#187; Quad</menuselection>

## Inputs

### `crlTargets`

- A _List of Cursor_ specifying the targets to check mesh quality. The targets can be part or face.
- This is a required input.

### `bStretchCheck`

- A _Boolean_ specifying to check the Stretch quality.

- The default value is 0.

### `bAspectRatioCheck`

- A _Boolean_ specifying to check the Aspect Ratio quality.

- The default value is 0.

### `bWarpingCheck`

- A _Boolean_ specifying to check the Warping quality.

- The default value is 0.

### `bSkewnessCheck`

- A _Boolean_ specifying to check the Skewness quality.

- The default value is 0.

### `bEdgeLengthCheck`

- A _Boolean_ specifying to check the Edge Length quality.

- The default value is 0.

### `bAreaCheck`

- A _Boolean_ specifying to check the Area quality.

- The default value is 0.

### `bNodeValenceCheck`

- A _Boolean_ specifying to check the Node Valence quality.

- The default value is 0.

### `bInteriorAngleCheck`

- A _Boolean_ specifying to check Interior Angle quality.

- The default value is 0.

### `bTaperCheck`

- A _Boolean_ specifying to check Taper quality.

- The default value is 0.

### `bDuplicateElemsCheck`

- A _Boolean_ specifying to check Duplicated Elements.

- The default value is 0.

### `dStretchLimit`

- A _Double_ specifying the threshold value of Stretch. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.
- The default value is 0.1.

### `dAspectRatioLimit`

- A _Double_ specifying the threshold value of Aspect Ratio. The elements with a stretch value greater than or equal to the specified value will be detected and displayed on the window.
- The default value is 10.

### `dWarpingLimit`

- A _Double_ specifying the threshold value of Warping. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.
- The default value is 1.

### `dSkewnessLimit`

- A _Double_ specifying the threshold value of Skewness. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.
- The default value is 70.

### `dEdgeLengthLimit`

- A _Double_ specifying the threshold value of Edge Length. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.
- The default value is 0.1.

### `dAreaLimit`

- A _Double_ specifying the threshold value of Area. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.
- The default value is 0.01.

### `dNodeValenceLimit`

- A _Double_ specifying the threshold value of Node Valence. The elements with a stretch value greater than or equal to the specified value will be detected and displayed on the window.
- The default value is 10.

### `dInteriorAngleLimit`

- A _Double_ specifying the threshold value of Interior Angle. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.
- The default value is 10.

### `dTaperLimit`

- A _Double_ specifying the threshold value of Tapper. The elements with a stretch value greater than or equal to the specified value will be detected and displayed on the window.
- The default value is 0.5.

## Return Code

A _Tuple_ specifying the elements's information that violated the mesh quality in order.
    1. Succeeded(1) or Failed(0)
    2. Number of error elements.
    3. A list of ID error elements.

## Sample Code

```psj {20-24}
# Prepare model
Geometry.Part.Cube(dlLength=[0.01, 0.01, 0.0001], 
                    ilAxialNodes=[10, 10, 2], 
                    iPartColor=7697908)
JPT.Exec("View Fit To Model()")
Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                    surfaceMesh=SURFACE_MESH(
                        dMaxElemSize=0.005, 
                        dMinElemSize=0.005, 
                        dGeomAngle=0.7853981634, 
                        dGradingFactor=0.5, iPerformanceMode=1, 
                        dAutoMergeTinyFacesAngle=0.5235987756, 
                        bOutputQuadMesh=True, 
                        bGeomApprox=True, 
                        iNextEntityOffsetId=0), 
                        bFMesher=True, 
                        iThreadNum=16)

# Check mesh quality
result = MeshCleanup.AutoCheck.Quad(crlTargets=[Part(1)], 
                                    bStretchCheck=True, 
                                    bWarpingCheck=True, 
                                    dStretchLimit=0.1, 
                                    dWarpingLimit=0.0174533)
if result[1] >=1:
    print("The number of error elements is " + str(result[1]))
    print("The error elements are " + str(result[2]))
else:
    print("There is no error element")
```
