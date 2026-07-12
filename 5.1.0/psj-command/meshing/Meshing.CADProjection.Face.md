---
id: Meshing-CADProjection-Face
title: Meshing.CADProjection.Face()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Project nodes of the meshed faces to the selected CAD (Reference) part
---

## Description

Project nodes of the meshed faces to the selected CAD (Reference) part.

## Syntax

```psj
Meshing.CADProjection.Face(...)
```

Ribbon: <menuselection>Meshing &#187; CAD Projection &#187; Face</menuselection>

## Inputs

### `crCadPart`

- A _Cursor_ specifying the CAD parts. Faces on selected parts will be the referenced faces for projection.
  - Note that for CAD part, _Cursor_ type will take different format from normal cursor's format.
    Two parameters are now needed: the former is ID (external id) and the latter is Key (internal id).
  - For example: RefPart((1,2)) means a CAD part with ID (external id) = 1 and Key (internal id) = 2.
- This is a required input.

### `crlMeshedFaces`

- A _List of Cursor_ specifying list of meshed faces. Nodes on these faces will be projected onto referenced faces.
- This is a required input.

### `bForceProject`

- A _Boolean_ specifying whether to force projection or not. If _True_, Jupiter will try to do projection more aggressively, hence may takes more time to finish.
- The default value is _False_.

### `bProjectCornerNodes`

- A _Boolean_ specifying whether to project corner nodes or not. If _True_, corner nodes of elements will be projected.
- The default value is _True_.

### `bProjectMidNodes`

- A _Boolean_ specifying whether to project mid nodes or not. If _True_, mid nodes of elements will be projected.
- The default value is _False_.

### `bIDcheck`

- A _Boolean_ specifying whether to check ID when projecting or not.
  - If _True_, nodes (on selected meshed faces) will only be projected to CAD faces (in the selected CAD Parts) whose ID is the same as the meshed face of those nodes. For example, if one node is on face 5, that node will only be projected to CAD face (in selected CAD Parts) with the same ID (i.e. 5).
  - If _False_, ID check will be skipped, and projection takes place when nodes and CAD faces (in the selected CAD parts) are at the closest distance.
- The default value is _False_.

## Return Code

A _Boolean_ specifying the status of the process:

- _True_: Projected the nodes of the meshed faces to the CAD (Reference) part.
- _False_: Cannot project the nodes of the meshed faces to the CAD (Reference) part.

## Sample Code

```psj {37,38,39,40}
Geometry.Part.Cylinder()
Geometry.Part.Cylinder(dlOrigin=[0.0, 0.0, 0.02], strName="Cylinder_2", iPartColor=6409934)

Geometry.FCircVertexAdjust(crlParts=[Part(1, 2)])
Meshing.SetMeshAttribute(crlParts=[Part(1, 2)],
                         surfaceMesh=SURFACE_MESH(dMaxElemSize=0.015,
                                                  dMinElemSize=0.0005,
                                                  dGeomAngle=0.7853981634,
                                                  dMinStretchVal=0.0,
                                                  iPerformanceMode=1,
                                                  dAutoMergeTinyFacesAngle=0.5235987756,
                                                  bGeomApprox=True,
                                                  iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(crlParts=[Part(1, 2)],
                       surfaceMesh=SURFACE_MESH(dMaxElemSize=0.015,
                                                dMinElemSize=0.0005,
                                                dGeomAngle=0.7853981634,
                                                dMinStretchVal=0.0,
                                                iPerformanceMode=1,
                                                dAutoMergeTinyFacesAngle=0.5235987756,
                                                bGeomApprox=True,
                                                iNextEntityOffsetId=0),
                       iThreadNum=4)

Meshing.SolidMeshing(crlParts=[Part(1, 2)],
                     bTet10=True,
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=4,
                     bInternalMeshOnly=False,
                     iPartColor=65280)

Meshing.CADProjection.Face(crCadPart=RefPart((2, 2)),
                           crlMeshedFaces=[Face(10)],
                           bProjectMidNodes=True,
                           bIDcheck=True)
```
