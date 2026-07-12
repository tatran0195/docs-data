---
id: Groups-RightClick-ChangeMarkerColor
title: Groups.RightClick.ChangeMarkerColor()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Change marker color of the group
---

## Description

Change marker color of the group.

## Syntax

```psj
Groups.RightClick.ChangeMarkerColor(...)
```

Ribbon: <menuselection>Groups &#187; RightClick &#187; Marker</menuselection>

## Inputs

### `list`

- List of pair of _Cursor_ and _color_ specifying the group and its marker color.
- The default value is _None_.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not
    - _True_: The process is executed successfully.
    - _False_:Cannot execute the function.

## Sample Code

```psj {11,12}
# Prepare model
Geometry.Part.Cube()

# Create groups
Tools.Group.CreateGroup(strGroupName="Group1", crlTargets=[Face(26)])
Tools.Group.CreateGroup(strGroupName="Group2", crlTargets=[Face(24)])

# Show marker color
JPT.Exec('ViewShowGroupMarker(1)')
# Change marker color
Groups.RightClick.ChangeMarkerColor(listGroupColors=[[Group(1), 10616736]])
Groups.RightClick.ChangeMarkerColor(listGroupColors=[[Group(2), 16716288]])
```
