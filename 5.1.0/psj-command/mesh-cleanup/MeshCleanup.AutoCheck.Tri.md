---
id: MeshCleanup-AutoCheck-Tri
title: MeshCleanup.AutoCheck.Tri()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Correct the surface mesh (TRI3/TRI6) by using multiple mesh quality standard
---

## Description

Correct the surface mesh (TRI3/TRI6) by using multiple mesh quality standard.

## Syntax

```psj
MeshCleanup.AutoCheck.Tri(...)
```

Macro:

Ribbon: <menuselection>MeshCleanup &#187; AutoCheck &#187; Tri</menuselection>

## Inputs

### `crlTargets`

- A _List of Cursor_ specifying the targets to check mesh quality. The targets can be part or face.
- This is a required input.

### `bStretchCheck`

- A _Boolean_ specifying to check the Stretch quality.

- The default value is 0.

### `bAspectRatioCheck`

- A _Boolean_ specifying to check Aspect Ratio quality.

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

### `bDuplicateElemsCheck`

- A _Boolean_ specifying to check Duplicated Elements.

- The default value is 0.

### `dStretchLimit`

- A _Double_ specifying the threshold value of Stretch. The elements with a stretch value less than or equal to the specified value will be detected and displayed on the window.
- The default value is 0.1.

### `dAspectRatioLimit`

- A _Double_ specifying the threshold value of Aspect Ratio. The elements with a stretch value greater than or equal to the specified value will be detected and displayed on the window.
- The default value is 10.

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

## Return Code

A _Tuple_ specifying the elements's information that violated the mesh quality in order.
    1. Succeeded(1) or Failed(0)
    2. Number of error elements.
    3. A list of ID error elements.

## Sample Code

```psj {19-21}
# Prepare model
Geometry.Part.Cube(dlLength=[0.01, 0.01, 0.0001], 
                    ilAxialNodes=[10, 10, 2], 
                    iPartColor=7697908)
Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                    surfaceMesh=SURFACE_MESH(
                        dAvgElemSize=0.001, 
                        dMinElemSize=0.0001, 
                        dGeomAngle=0.7853981634, 
                        dGeomMinSize=0.0001, 
                        dGradingFactor=0.5, 
                        iPerformanceMode=1, 
                        dAutoMergeTinyFacesAngle=0.5235987756, 
                        bGeomApprox=True, 
                        iNextEntityOffsetId=0), 
                        iThreadNum=16)

# Check mesh quality
result = MeshCleanup.AutoCheck.Tri(crlTargets=[Part(1)], 
                                bEdgeLengthCheck=True, 
                                dEdgeLengthLimit=0.0001)
if result[1] >=1:
    print("The number of error elements is " + str(result[1]))
    print("The error elements are " + str(result[2]))
else:
    print("There is no error element")
```
