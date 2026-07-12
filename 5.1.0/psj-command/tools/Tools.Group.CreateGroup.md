---
id: Tools-Group-CreateGroup
title: Tools.Group.CreateGroup()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a group of arbitrary entities.
---

## Description

Create a group of arbitrary entities.

## Syntax

```psj
Tools.Group.CreateGroup(strGroupName, crlTargets=[], crEdit=None)
```

Ribbon: <menuselection>Tools &#187; Group &#187; CreateGroup</menuselection>

## Inputs

### `strGroupName`

- A _String_ specifying the group name.
- This is a required input.

### `crlTargets`

- A _List of Cursor_ specifying the target.
- The default value is [].

### `crEdit`

- A _Cursor_ specifying the edit.
- The default value is None.

## Return Code

A _List of Cursor_ specifying the created group.

## Sample Code

```psj {2}
Geometry.Part.Cube(iPartColor=6409934)
created_group = Tools.Group.CreateGroup(strGroupName="Part_Group1", crlTargets=[Part(1)])
for group in created_group:
    JPT.Debugger(JPT.MacroTCursorToDItem(str(group)))
```
