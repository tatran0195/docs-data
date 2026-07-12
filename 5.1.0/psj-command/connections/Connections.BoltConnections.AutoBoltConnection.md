---
id: Connections-BoltConnections-AutoBoltConnection
title: Connections.BoltConnections.AutoBoltConnection()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create bolt connection for all the detected bolt holes at one time
---

## Description

Create bolt connection for all the detected bolt holes at one time

## Syntax

```psj
Connections.BoltConnections.AutoBoltConnection(...)
```

Macro: AutoBoltConnection

Ribbon: <menuselection>Connections &#187; BoltConnections &#187; AutoBoltConnection</menuselection>

## Inputs

### `strName`

- A _String_ specifying the bolt connection name.
- This is a required input.

### `listBoltHoles`

- A _list of [BOLT_HOLE_FACE](./../../data-type/psj-command/parameter-types/BOLT_HOLE_FACE)_ specifying data of bolt hole face.  
- This is a required input.

### `crlMatingFaces`

- A _List of Cursor_ specifying mating faces target.
- This is a required input.

### `boltTypeA`

- A _BOLT_TYPE_AB_ specifying an instance of BOLT_TYPE_AB class specifying the information of bolt type A and B
- The default value is BOLT_TYPE_AB().
 
  
### `boltTypeB`

- A _BOLT_TYPE_AB_ specifying an instance of BOLT_TYPE_AB class specifying the information of bolt type A and B
- The default value is BOLT_TYPE_AB().

### `boltTypeC`

- A _Boolean_ specifying an instance of BOLT_TYPE_C class specifying the information of bolt type C
- The default value is BOLT_TYPE_C().

### `boltTypeD`

- A _Boolean_ specifying an instance of BOLT_TYPE_D class specifying the information of bolt type D
- The default value is BOLT_TYPE_D().
  
### `bLocalSettingFace`

- A _Boolean_ specifying the local setting face option
- The default value is _False_.

### `dLocalSettingSize`

- A _Double_ specifying the local setting size.
- The default value is 0.003.

## Return Code

- A _Boolean_ specifying the function succeeded or not.
  - True: Succeeded
  - False: Failed

## Sample Code

```psj {19-23}
Geometry.Part.Cylinder(bHollow=True, 
  dTopInnerRadius=0.002, 
  dBottomInnerRadius=0.002, 
  iPartColor=6250447)
Geometry.Part.Cylinder(
  strName="Cylinder_2", 
  bHollow=True, 
  dlOrigin=[0.0, 0.01, 0.0], 
  dTopInnerRadius=0.002, 
  dBottomInnerRadius=0.002, 
  iPartColor=12537679)

Connections.BoltConnections.FindAutoBoltConnection(
  crMasterPart=Part(2), 
  crSlavePart=Part(1), 
  dMinCircleDiameter=0.00368, 
  dMaxCircleDiameter=0.0045)
ret = Connections.BoltConnections.AutoBoltConnection(
    strName="Bolt", 
    listBoltHoles=[BOLT_HOLE_FACE(crlMasterFaces=[Face(15)], crlSlaveFaces=[Face(7)], 
    dlCenterPoint=[0, 0.01, 0], 
    dlMasterPoint=[0, 0.02, 0])], 
    crlMatingFaces=[Face(14, 5)])
print(ret)
```
