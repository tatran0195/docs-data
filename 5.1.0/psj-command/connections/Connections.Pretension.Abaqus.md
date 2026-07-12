---
id: Connections-Pretension-Abaqus
title: Connections.Pretension.Abaqus()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create bolt pretension for the Abaqus solver
---

## Description

Create bolt pretension for the Abaqus solver.

## Syntax

```psj
Connections.Pretension.Abaqus(...)
```

Macro: [PretensionAbaqus](../../macro/connections/PretensionAbaqus)

Ribbon: <menuselection>Connections &#187; Pretension &#187; Abaqus</menuselection>

## Inputs

### `crTargets`

- A _Cursor_ specifying the faces or the element for creating the pretension force.
- This is a required input.

### `dForceValue`

- A _Double_ specifying the value of pretension force.
- This is a required input.

### `dlForceDirection`

- A _List of Double_ specifying the direction of pretension force.
- This is a required input.

### `dlControlNode`

- A _List of Double_ specifying the position of the control node.
- This is a required input.

### `strName`

- A _String_ specifying the name of pretension force.
- The default value is "PreTensionAbaqus1".

### `bFixedLength`

- A _Boolean_ specified whether or not the tightening force of the bolt option are retained.
- The default value is _False_.

### `crLbcConstraint`

- A _Cursor_ specifying the existing Fixed Constraint object of pretension force to be edited. This argument must be specified when _crLbcPretensionAbaqus_ is specified. Otherwise, a new Fixed Constraint object will be created.
- The default value is _None_.

### `crLbcPretensionAbaqus`

- A _Cursor_ specifying an existing pretension force (Abaqus). If no pretension force is specified, a new one will be created, otherwise, the specified pretension force (Abaqus) will be modified.
- The default value is _None_.

### `iRefNodeID`

- An _Int_ specified the reference node.
- This is a required input.

## Return Code

A _Cursor_ specifying the created Abaqus pretension.

## Sample Code

```psj {31,32,33,34,35,36,37,38}
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

max_node_id=JPT.GetMaxIDEntity(JPT.EntityType.NODE)

creating_status = Connections.Pretension.Abaqus(crlTargets=[Face(11)], 
                                                dForceValue=1000000.0, 
                                                dlForceDirection=[0.000000,
                                                                  -1.000000,
                                                                  0.000000],
                                                dlControlNode=[0.001419156, 
                                                               0.02, 
                                                               0.00012416],
                                                iRefNodeID=max_node_id+1)

JPT.Debugger(creating_status)
```
