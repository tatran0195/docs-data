---
id: MeshCleanup.Manual3D.Collapse.CenterElementCollapse
title: MeshCleanup.Manual3D.Collapse.CenterElementCollapse()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Collapse the selected element towards the center of its element and connect the surrounding elements
---

## Description

Collapse the selected element towards the center of its element and connect the surrounding elements.

## Syntax

```psj
MeshCleanup.Manual3D.Collapse.CenterElementCollapse(...)
```

Macro: 

Ribbon: <menuselection>MeshCleanup &#187; Manual3D &#187; Collapse &#187; CenterElementCollapse</menuselection>

## Inputs

### `crlElems`

- A _List of Cursor_ specifying the solid element.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {11}
Geometry.Part.Cube(iPartColor=6409934)
Meshing.SolidMeshing(crlParts=[Part(1)], 
                    dGradingFactor=1.05, 
                    dStretchLimit=0.1, 
                    iSpeedVsQual=1, 
                    iRegion=1, 
                    bSafeMode=False, 
                    iParallel=16, 
                    bInternalMeshOnly=False, 
                    iPartColor=65280)
MeshCleanup.Manual3D.Collapse.CenterCollapse(crlElems=[Elem(8756)])
```
