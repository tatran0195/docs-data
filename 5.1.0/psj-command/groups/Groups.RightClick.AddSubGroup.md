---
id: Groups-RightClick-AddSubGroup
title: Groups.RightClick.AddSubGroup()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a sub group to the Group tree in the Group Window
---

## Description

Create a sub group to the Group tree in the Group Window.

## Syntax

```psj
Groups.RightClick.AddSubGroup(...)
```

Ribbon: <menuselection>Groups &#187; RightClick &#187; AddSubGroup</menuselection>

## Inputs

### `crSubGroupSelected`

- A _Cursor_ specifying the master subgroup to add a sub group onto.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created sub group.

## Sample Code

```psj {9}
# Prepare model
Geometry.Part.Cube()

# Create groups
Tools.Group.CreateGroup(strGroupName="Group1", crlTargets=[Face(26)])
Tools.Group.CreateGroup(strGroupName="Group2", crlTargets=[Face(24)])

# Add subgroups
created_sub_group = Groups.RightClick.AddSubGroup()
Assembly.RightClick.Rename(strNewName="SubGroup - 1", crItem=SubGroup(1))
JPT.Debugger(created_sub_group)
```
