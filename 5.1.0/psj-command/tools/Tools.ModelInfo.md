---
id: Tools-ModelInfo
title: Tools.ModelInfo()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: export model info file
---

## Description

Export model info file

## Syntax

```psj
Tools.ModelInfo(strPath, strPathName="", listMeshPartInfoTool=[], bPropertyAssignedPart=False, bPropertyAssignedSummary=False, iModelNode=0, iNmodelnodeWithprop=0, ilModelElement=[], ilNmodelelemWithprop=[], ilModelLBC=[], iModelContact=0, ilModelConnection=[], ilModelProperty=[])
```

Ribbon: <menuselection>Tools &#187; ModelInfo</menuselection>

## Inputs

### `strPath`

- A _String_ specifying the path.
- This is a required input.

### `strPathName`

- A _String_ specifying the path name.
- The default value is "".

### `listMeshPartInfoTool`

- A _MESH_PART_INFO_TOOL List_ specifying the mesh part info tool.
- The default value is [].

### `bPropertyAssignedPart`

- A _Boolean_ specifying the property assigned part.
- The default value is False.

### `bPropertyAssignedSummary`

- A _Boolean_ specifying the property assigned summary.
- The default value is False.

### `iModelNode`

- An _Integer_ specifying the model node.
- The default value is 0.

### `iNmodelnodeWithprop`

- An _Integer_ specifying the nmodelnode withprop.
- The default value is 0.

### `ilModelElement`

- A _List of Integer_ specifying the model element.
- The default value is [].

### `ilNmodelelemWithprop`

- A _List of Integer_ specifying the nmodelelem withprop.
- The default value is [].

### `ilModelLBC`

- A _List of Integer_ specifying the model load boundary condition.
- The default value is [].

### `iModelContact`

- An _Integer_ specifying the model contact.
- The default value is 0.

### `ilModelConnection`

- A _List of Integer_ specifying the model connection.
- The default value is [].

### `ilModelProperty`

- A _List of Integer_ specifying the model property.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.ModelInfo(strPath, strPathName="", listMeshPartInfoTool=[], bPropertyAssignedPart=False, bPropertyAssignedSummary=False, iModelNode=0, iNmodelnodeWithprop=0, ilModelElement=[], ilNmodelelemWithprop=[], ilModelLBC=[], iModelContact=0, ilModelConnection=[], ilModelProperty=[])
```
