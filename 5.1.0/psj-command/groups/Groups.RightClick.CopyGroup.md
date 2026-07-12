---
id: Groups-RightClick-CopyGroup
title: Groups.RightClick.CopyGroup()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Copy the inputted groups in the Group tree and paste them to a specified sub group
---

## Description

Copy the inputted groups in the Group tree and paste them to a specified sub group.

## Syntax

```psj
Groups.RightClick.CopyGroup(...)
```

Ribbon: <menuselection>Groups &#187; RightClick &#187; CopyGroup</menuselection>

## Inputs

### `crlGroups`

- A _List of Cursor_ specifying the list of group items uses for copying.
- This is a required input.

### `strlNames`

- A _List of String_ specifying the list of new group names for the copied groups.
- The default value is [].

### `crSubGroup`

- A _Cursor_ specifying the supper group destination if any.
- The default value is _None_.

### `bKeepOriginalGroup`

- A _Boolean_ enable/disable the keeping original group.
- The default value is _False_.

## Return Code

A _List of Cursor_ specifying all the pasted groups.

## Sample Code

```psj {12,13}
Geometry.Part.Cube()

Tools.Group.CreateGroup(strGroupName="Group1", 
                        crlTargets=[Face(22)])
Tools.Group.CreateGroup(strGroupName="Group2", 
                        crlTargets=[Face(24)])
Tools.Group.CreateGroup(strGroupName="Group3",
                        crlTargets=[Face(26)])

Groups.RightClick.AddSubGroup()

pasted_groups = Groups.RightClick.CopyGroup(crlGroups=[Group(1, 2, 3)], 
                                            crSubGroup=SubGroup(1))

JPT.Debugger(pasted_groups)
```
