---
id: Meshing-BarMeshing
title: Meshing.BarMeshing()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Mesh 1D edge/bar part
---

## Description

Mesh 1D edge/bar part.

## Syntax

```psj
Meshing.BarMeshing(...)
```

Macro: [BeamMeshing](../../macro/meshing/BeamMeshing)

Ribbon: <menuselection>Meshing &#187; BarMeshing</menuselection>

## Inputs

### `crlCadEdge`

- A _List of Cursor_ specifying list of CAD edges.
- This is a required input.

### `crlBarEdge`

- A _List of Cursor_ specifying list of bar edges.
- This is a required input.

### `crlBarPart`

- A _List of Cursor_ specifying list of bar parts./
- This is a required input.

### `dDocMeshSize`

- A _Double_ specifying desired mesh size.
- The default value is 0.

### `iDocNumofElem`

- An _Integer_ specifying desired number of elements. If this parameter is bigger than 0 , `dDocMeshSize` is ignored.
- The default value is 4.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {9,10,11,12}
MeshEdit.CreateNode.Absolute(veclNodeCoord=[[0.0, 0.0, 0.0]], 
                             ilNewNodeID=[1])
MeshEdit.CreateNode.Absolute(veclNodeCoord=[[0.001, 0.0, 0.0]], 
                             ilNewNodeID=[2])
Geometry.Bar.TwoNodes(iMeshCount=1, 
                      crStartNode=Node(2), 
                      crEndNode=Node(1))

mesh_status = Meshing.BarMeshing(crlCadEdge=[], 
                                 crlBarEdge=[1], 
                                 crlBarPart=[], 
                                 iDocNumofElem=10)

JPT.Debugger(mesh_status)
```
