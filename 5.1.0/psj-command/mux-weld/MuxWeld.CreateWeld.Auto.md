---
id: MuxWeld-CreateWeld-Auto
title: MuxWeld.CreateWeld.Auto()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Auto create weld
---

## Description

Auto create weld

## Syntax

```psj
MuxWeld.CreateWeld.Auto(iIconnectattributeMethod, strStrconnectattributeName, crlMasterTargets, crlSlaveTargets, iIconnectattributeCoordsys, crEdit)
```

Ribbon: <menuselection>MuxWeld &#187; CreateWeld &#187; Auto</menuselection>

## Inputs

### `iIconnectattributeMethod`

- An _Integer_ specifying the iconnectattribute method.
- This is a required input.

### `strStrconnectattributeName`

- A _String_ specifying the strconnectattribute name.
- This is a required input.

### `crlMasterTargets`

- A _List of Cursor_ specifying the master target.
- This is a required input.

### `crlSlaveTargets`

- A _List of Cursor_ specifying the slave target.
- This is a required input.

### `iIconnectattributeCoordsys`

- An _Integer_ specifying the iconnectattribute coordsys.
- This is a required input.

### `crEdit`

- A _Cursor_ specifying the edit.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MuxWeld.CreateWeld.Auto(iIconnectattributeMethod, strStrconnectattributeName, crlMasterTargets, crlSlaveTargets, iIconnectattributeCoordsys, crEdit)
```
