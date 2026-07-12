---
id: Groups-RightClick-Rename
title: Groups.RightClick.Rename()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Rename the specified group in the Group tree of the Group Window
---

## Description

Rename the specified group in the Group tree of the Group Window.

## Syntax

```psj
Groups.RightClick.Rename(...)
```

Ribbon: <menuselection>Groups &#187; RightClick &#187; Rename</menuselection>

## Inputs

### `strNewName`

- A _String_ specifying the new name of the group to be renamed.
- This is a required input.

### `crItem`

- A _Cursor_ specifying the current group to be renamed.
- This is a required input.

## Return Code

A _Boolean_ specifying the status of the deleting process:

- _True_: The name of the inputted group has been changed successfully.
- _False_: The name of the inputted group cannot be changed.

## Sample Code

```psj {5}
Geometry.Part.Cube()

Tools.Group.CreateGroup(strGroupName="Group1", crlTargets=[Part(1)])

rename_status = Groups.RightClick.Rename(strNewName = "new name", crItem = Group(1))

JPT.Debugger(rename_status)
```
