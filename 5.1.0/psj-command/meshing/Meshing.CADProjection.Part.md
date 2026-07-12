---
id: Meshing-CADProjection-Part
title: Meshing.CADProjection.Part()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Project nodes of the meshed part to the selected CAD (Reference) part.
---

## Description

Project nodes of the meshed part to the selected CAD (Reference) part.

## Syntax

```psj
Meshing.CADProjection.Part(crCadPart,
                           crMeshedPart,
                           bProjectCornerNodes=False,
                           bProjectMidNodes=True,
                           bIDcheck=True)
```

Ribbon: <menuselection>Meshing &#187; CADProjection &#187; Part</menuselection>

## Inputs

### `crCadPart`

- A _Cursor_ specifying the CAD Parts. CAD Faces in these parts will be the reference faces for projection.
  - Note that for CAD part, _Cursor_ type will take different format from normal cursor's format. Two parameters are now needed: the former is ID (external id) and the latter is Key (internal id).
  - For example: RefPart((1,2)) means a CAD part with ID (external id) = 1 and Key (internal id) = 2.
- This is a required input.

### `crMeshedPart`

- A _Cursor_ specifying the Meshed Parts. Meshed Faces in these parts will be projected onto reference faces.
- This is a required input.

### `bProjectCornerNodes`

- A _Boolean_ to enable/disable corner nodes projection. If _True_, corner nodes of elements will be projected.
- The default value is _False_.

### `bProjectMidNodes`

- A _Boolean_ to enable/disable mid nodes projection. If _True_, mid nodes of elements will be projected.
- The default value is _True_.

### `bIDcheck`

- A _Boolean_ to enable/disable ID check when projecting.
- The default value is _True_.

## Return Code

A _Boolean_ specifying the status of the process:

- _True_: Projected the nodes of the meshed part to the CAD (Reference) part.
- _False_: Cannot project the nodes of the meshed part to the CAD (Reference) part.

## Sample Code

```psj {33,34,35}
cyl=Geometry.Part.Cylinder()

Meshing.SetMeshAttribute(crlParts=[cyl],
                         surfaceMesh=SURFACE_MESH(dMinElemSize=0.0005,
                                                  dGeomAngle=0.7853981634,
                                                  dGeomMinSize=0.0005,
                                                  iPerformanceMode=1,
                                                  dAutoMergeTinyFacesAngle=0.5235987756,
                                                  bGeomApprox=True,
                                                  iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(crlParts=[cyl],
                       surfaceMesh=SURFACE_MESH(dMinElemSize=0.0005,
                                                dGeomAngle=0.7853981634,
                                                dGeomMinSize=0.0005,
                                                iPerformanceMode=1,
                                                dAutoMergeTinyFacesAngle=0.5235987756,
                                                bGeomApprox=True,
                                                iNextEntityOffsetId=0),
                       iThreadNum=4)

Meshing.SolidMeshing(crlParts=[cyl],
                     bTet10=True,
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=4,
                     bInternalMeshOnly=False,
                     iPartColor=65280)

Meshing.CADProjection.Part(crCadPart=RefPart((1,1)),
                           crMeshedPart=cyl,
                           bProjectCornerNodes=True)
```
