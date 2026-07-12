---
id: Connections-MPC-Equation-SemiAuto
title: Connections.MPC.Equation.SemiAuto()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Creates the MPC between the nodes with a distance tolerance
---

## Description

Creates the MPC between the nodes with a distance tolerance.

## Syntax

```psj
Connections.MPC.Equation.SemiAuto(...)

```

Macro: [Mpc](../../macro/connections/Mpc)

Ribbon: <menuselection>Connections &#187; MPC &#187; Equation &#187; SemiAuto</menuselection>

## Inputs

### `strName`

- A _String_ specifying the MPC name.
- The default value is "MPC_1".

### `crlMasterEntities`

- A _List of Cursor_ specifying the list of master entities. The entities could be any of types such as Parts/Faces/Edges/Nodes.
- This is the required input.

### `crlSlaveEntities`

- A _List of Cursor_ specifying the list of slave entities. The entities could be any of types such as Parts/Faces/Edges/Nodes.
- This is the required input.

### `listMpcConnection`

- A _List of [MPC_CONNECTION](./../../data-type/psj-command/parameter-types/MPC_CONNECTION)_ specifying the list of MPC connection.
- The default value is [].

### `dConstantValue`

- A _Double_ specifying the MPC value.
- The default value is 0.0.

### `iLocalCoordinate`

- An _Integer_ specifying the coordinate system.
- The default value is 0.

### `bUpdateDispCS`

- A _Boolean_ specifying whether or not update displacement coordinate system.
- The default value is _True_.

### `crMpcConnection`

- A _Cursor_ specifying an existing contact setting (MPC Equation). If this parameter is used, the specified contact setting (MPC Equation) will be modified. When the default value is used, a new contact setting (MPC Equation) will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created or the modified contact connection.

## Sample Code

```psj {6,7,8,9,10,11,12,13}
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=12867524)

created_mpc = Connections.MPC.Equation.SemiAuto(crlMasterEntities=[Face(24)], 
                                                crlSlaveEntities=[Face(49)], 
                                                listMpcConnection=[MPC_CONNECTION(dCoef=20.0, 
                                                                                  iDof=1), 
                                                                   MPC_CONNECTION(dCoef=-20.0, 
                                                                                  iDof=1)], 
                                                dConstantValue=10.0, 
                                                bUpdateDispCS=1)

JPT.Debugger(created_mpc)
```
