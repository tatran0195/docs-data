---
id: Connections-Pretension-Advc
title: Connections.Pretension.Advc()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create bolt pretension for the ADVC solver
---

## Description

Create bolt pretension for the ADVC solver.

## Syntax

```psj
Connections.Pretension.Advc(...)
```

Ribbon: <menuselection>Connections &#187; Pretension &#187; Advc</menuselection>

## Inputs

### `crlTargets`

- A _List of Cursor_ specifying the list of targets. It can be faces or 1D elements.
- This is a required input.

### `dForceValue`

- A _Double_ specifying the value of pretension force.
- This is a required input.

### `dlForceDirection`

- A _List of Double_ specifying the bolt tightening direction.
- This is a required input.

### `dlControlNode`

- A _List of Double_ specifying the position of control node.
- This is a required input.

### `strName`

- A _String_ specifying the name of pretension force.
- The default value is "PreTensionAdvc1".

### `bFixedLength`

- A _Boolean_ specified whether or not the tightening force of the bolt option are retained.
- The default value is _False_.

### `crLbcEnforcedVelocity`

- A _Cursor_ specifying the existing enforced velocity of the pretension force (ADVC) to be edited. This argument must be specified when _crLbcPretensionADVC_ is specified.
- The default value is _None_.

### `iDirectionUpdate`

- An _Integer_ specifying whether or not the tightening direction has been updated.
  - If _iDirectionUpdate=0_, this argument is ignored.
  - If _iDirectionUpdate=1_, update the tightening direction.
  - If _iDirectionUpdate=2_, do not update the tightening direction.
- The default value is 0.

### `iRefNodeId`

- An _Integer_ specifying the ID of reference node.
- The default value is 0.

### `crLbcPretensionADVC`

- A _Cursor_ specifying an existing pretension force (ADVC). 
  - If this parameter is used, the specified pretension force (ADVC) will be modified.
  - If it is left _None_, a new pretension force (ADVC) will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created ADVC pretension.

## Sample Code

```psj {31,32,33,34,35}
Geometry.Part.Cylinder(dHeight=0.04,
                       iPartColor=6447843)
MeshEdit.CreateNode.Between2Nodes(iNodeID=363,
                                  dX=7.66044e-06, 
                                  dY=2e-05, 
                                  dZ=-6.42788e-06, 
                                  iNumberofNodes=1, 
                                  crlNodes=[Node(65, 
                                                 66)])
MeshEdit.CreateNode.Between2Nodes(iNodeID=364, 
                                  dX=-1.73648e-06, 
                                  dY=2e-05, 
                                  dZ=9.84808e-06, 
                                  iNumberofNodes=1, 
                                  crlNodes=[Node(21, 
                                                 22)])
MeshEdit.CreateNode.Between2Nodes(iNodeID=365, 
                                  dX=-3.4202e-06, 
                                  dY=2e-05, 
                                  dZ=-9.39693e-06, 
                                  iNumberofNodes=1, 
                                  crlNodes=[Node(51, 
                                                 52)])
Geometry.BodyCut.By3Points(crPart=Part(1), 
                           poslPoints=[[-0.003420201433256686, 0.02, -0.009396926207859084], 
                                       [0.007660444431189778, 0.02, -0.006427876096865396], 
                                       [-0.001736481776669303, 0.02, 0.00984807753012208]], 
                           bSplitOnly=True)
MeshEdit.DeleteNode()

creating_status = Connections.Pretension.Advc(crlTargets=[Face(8)], 
                                              dForceValue=1.0, 
                                              dlForceDirection=[0.0, -1.0, 0.0], 
                                              dlControlNode=[0.001419156, 0.02, 0.00012416],
                                              iRefNodeId=442)
JPT.Debugger(creating_status)
```
