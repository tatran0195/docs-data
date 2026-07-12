---
id: Groups-RightClick-ExportGroup
title: Groups.RightClick.ExportGroup()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Export specified group to *CSV file.
---

## Description

Export specified group to *CSV file.

## Syntax

```psj
Groups.RightClick.ExportGroup(...)
```

Macro: 

Ribbon: <menuselection>Groups &#187; RightClick &#187; ExportGroup</menuselection>

## Inputs

### `crlTargets`

- A _List of Cursor_ specifying the groups to be exported.
- This is a required input.

### `strlPaths`

- A _List of String_ specifying the paths of *CSV files.
- This is a required input.

### `iEncode`

- An _Integer_ specifying encoding type.
    - -1: None
    - 0: UTF-8
    - 1: SHIFT-JIS
- The default value is -1.

### `bWithBOM`

- A _Boolean_ specifying whether or not include BOM for UTF-8 format.
- The default value is _False_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: Export the group successfully.
    - _False_: Cannot export the group.

## Sample Code

```psj {19-23}
import os 

# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
Tools.Group.CreateGroup(
    strGroupName="Group1", 
    crlTargets=[Face(26, 24)])
JPT.ViewFitToModel()

Tools.Group.CreateGroup(
    strGroupName="Group2", 
    crlTargets=[Node(45, 46, 100, 101, 102, 145, 146, 153, 154)])

temp_path=JPT.GetAppPathInfo(JPT.PathType.TEMP_PATH)

groups=JPT.GetAllGroups()
for group in groups:
    # Export groups
    Groups.RightClick.ExportGroup(
        crlTargets=[Group(group.id)], 
        strlPaths=[os.path.join(temp_path,f"Group_{group.id}.csv")],
        iEncode=1,
        bWithBOM=True)
```
