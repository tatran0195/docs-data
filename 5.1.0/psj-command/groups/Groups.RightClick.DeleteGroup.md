---
id: Groups-RightClick-DeleteGroup
title: Groups.RightClick.DeleteGroup()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Delete specified groups from the Group tree in the Group Window
---

## Description

Delete specified groups from the Group tree in the Group Window.

## Syntax

```psj
Groups.RightClick.DeleteGroup(...)
```

Ribbon: <menuselection>Groups &#187; RightClick &#187; DeleteGroup</menuselection>

## Inputs

### `crlGroups`

- A _List of Cursor_ specifying the list of group items uses for deleting.
- This is a required input.

### `bRemoveAll`

- A _Boolean_ enable/disable all group deletion.
- The default value is _False_.

## Return Code

A _Boolean_ specifying the status of the deleting process:

- _True_: The inputted groups have been deleted successfully.
- _False_: The inputted groups cannot be deleted.

## Sample Code

```psj {8,9}
Geometry.Part.Cube()

Tools.Group.CreateGroup(strGroupName="Group1",
                        crlTargets=[Face(26)])
Tools.Group.CreateGroup(strGroupName="Group2",
                        crlTargets=[Face(24)])

deleted_groups = Groups.RightClick.DeleteGroup(crlGroups=[Group(1,
                                                                2)])

JPT.Debugger(deleted_groups)
```
