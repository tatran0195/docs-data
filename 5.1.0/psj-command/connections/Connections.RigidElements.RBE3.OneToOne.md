---
id: Connections-RigidElements-RBE3-OneToOne
title: Connections.RigidElements.RBE3.OneToOne()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create one to one (Slave:Master) RBE3 (Interpolation constraining Element)
---

## Description

Create one to one (Slave:Master) RBE3 (Interpolation constraining Element).

## Syntax

```psj
Connections.RigidElements.RBE3.OneToOne(...)
```

Ribbon: <menuselection>Connections &#187; RigidElements &#187; RBE3 &#187; OneToOne</menuselection>

## Inputs

### `iMethod`

- An _Integer_ specifying the method.
- The default value is 17.

### `crlMasterTargets`

- A _List of Cursor_ specifying the master target.
- The default value is [].

### `crlSlaveTargets`

- A _List of Cursor_ specifying the slave target.
- The default value is [].

### `listRbe3TermConnection`

- A _RBE3TERM_CONNECTION List_ specifying the rbe3 term connection.
- The default value is [].

### `iTypeRBE3`

- An _Integer_ specifying the type r e3.
- The default value is 3.

### `strName`

- A _String_ specifying the name.
- The default value is "".

### `crCoordSys`

- A _Cursor_ specifying the coordinate system.
- The default value is None.

### `dTolerance`

- A _Double_ specifying the tolerance.
- The default value is 0.0.

### `dlVirtualNodePos`

- A _Double List_ specifying the virtual node position.
- The default value is [0, 0, 0].

### `iSurfaceDef`

- An _Integer_ specifying the surface definition.
- The default value is 0.

### `crEdit`

- A _Cursor_ specifying the edit.
- The default value is None.

### `bUpdateDispCS`

- A _Boolean_ specifying the enable update displacement coordinate system.
- The default value is _True_.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {11-15}
Geometry.Part.Cube(
    ilAxialNodes=[4, 4, 4], strName="Cube_2", iPartColor=14903267)

Geometry.Part.Cube(
    dlOrigin=[0.012, 0.0, 0.0], 
    ilAxialNodes=[4, 4, 4], 
    strName="Cube_3", 
    iPartColor=7829501)

Connections.RigidElements.RBE3.OneToOne(
    crlMasterTargets=[Node(61, 87, 88, 64, 57, 71, 72, 60)], 
    crlSlaveTargets=[Node(6, 27, 28, 7, 2, 11, 12, 3)],
     listRbe3TermConnection=[(0, 63, 8), (1, 7, 8)],
     strName="RBE3_3")
```
