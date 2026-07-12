---
id: Geometry-ShapeSearch
title: Geometry.ShapeSearch()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Search shape in specified parts.
---

## Description

Search shape in specified parts.

## Syntax

```psj
Geometry.ShapeSearch(...)
```

Macro: 

Ribbon: <menuselection>Geometry &#187; ShapeSearch</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the target parts.
- This is a required input.

### `crlRefEdges`

- A _List of Cursor_ specifying the reference edges.
- The default value is [].

### `iGroupOption`

- An _Integer_ specifying the grouping option.
    - 0: Do not create the Group.
    - 1: Create a group containing all searched results (faces, edges) of all specified shape types for searching in the selected parts.
    - 2: Create separate groups containing the searched results (faces, edges) corresponding to each specified shape type for searching in the selected parts.
- The default value is 0.

### `strGroupName`

- A _String_ specifying the name of the group.
- The default value is "".

### `listShapeSearchOptions`

- A _List of SHAPE_SEARCH_OPTION_  specifying the geometry options required for searching.
- The default value is _[SHAPE_SEARCH_OPTION](../../data-type/psj-command/parameter-types/SHAPE_SEARCH_OPTION)_.

### `bConvexOption`

- A _Boolean_ specifying whether to include convex shapes.
- The default value is _False_.
  
### `bConcaveOption `

- A _Boolean_ specifying whether to include concave shapes.
- The default value is _False_.

## Return Code

- A _List of Cursor_ specifying the entities (face or edge) found.
 
## Sample Code

```psj {7,12}
# Prepare model
Geometry.Part.Cylinder(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], iPartColor=7434735)

JPT.ClearAllSelection()
# Search planar faces and select.
result=Geometry.ShapeSearch(crlParts=[Part(1, 2)], listShapeSearchOptions=[SHAPE_SEARCH_OPTION(iType=4, bAll=1)])
print(f"There are {len(result)} planar faces.")

JPT.ClearAllSelection()
# Search full cylinder faces and select.
result=Geometry.ShapeSearch(crlParts=[Part(1, 2)], listShapeSearchOptions=[SHAPE_SEARCH_OPTION(iType=8, bAll=1)])
print(f"There are {len(result)} full cylinder faces.")
```
