---
id: JPT-IsSpatialPointRendered
title: JPT.IsSpatialPointRendered()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Check if a specified point (node) that has the spatial coordinates (X, Y, Z) is rendered in the current view
---

## Description

Check if a specified point (node) that has the spatial coordinates (X, Y, Z) is rendered in the current view.

## Syntax

```psj
JPT.IsSpatialPointRendered(posX, posY, posZ)
```

## Inputs

### `posX`

- A _Double_ specifying the X coordinate of the specified point (node).
- This is a required input.

### `posY`

- A _Double_ specifying the Y coordinate of the specified point (node).
- This is a required input.

### `posZ`

- A _Double_ specifying the Z coordinate of the specified point (node).
- This is a required input.

## Return Code

A _Boolean_ specifying the status of the specified point (node):
- _True_: The specified point (node) can be rendered.
- _False_: The specified point (node) is hidden.

## Sample Code

```psj {10}
# Prepare model
Geometry.Part.Cube(iPartColor=6974164)
JPT.ViewFitToModel()

# Select a node with ID = 7
JPT.SelectionByID(JPT.DItemType.NODE, 7, True)
listSelNodes = JPT.GetSelectedNodes()

# Check if the selected node is rendered
result=JPT.IsSpatialPointRendered(listSelNodes[0].pos.x, listSelNodes[0].pos.y, listSelNodes[0].pos.z)
print(result)
```
