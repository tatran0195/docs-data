---
id: Tools-Measure-Distance-TwoNodes
title: Tools.Measure.Distance.TwoNodes()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Measure distance between two nodes
---

## Description

Measure distance between two nodes.

## Syntax

```psj
Tools.Measure.Distance.TwoNodes(...)
```

Ribbon: <menuselection>Tools &#187; Measure &#187; Distance &#187; TwoNodes</menuselection>

## Inputs

### `crNode1`

- A _Cursor_ specifying the first node to measure distance.
- This is a required input.

### `crNode2`

- A _Cursor_ specifying the second node to measure distance.
- This is a required input.

### `strTarget`

- A _String_ specifying the target projection axis, or the three-dimensional space (3D) to refer to measure. This parameter can be one of the following:
  - If _strTarget="X"_: Return the distance value along the X axis.
  - If _strTarget="Y"_: Return the distance value along the Y axis.
  - If _strTarget="Z"_: Return the distance value along the Z axis.
  - If _strTarget="Dist"_: Return the angle value on in 3D space.
  - If _strTarget="All"_: Return all the 4 distance values in a list, in order "Dist", "X", "Y", "Z".
- The default value is "All".

### `iPrecision`

- An _Integer_ specifying the number of digit after floating point. The greater `iPrecision` could be, the more accuracy of distance can be measured.
- The default value is 6.

### `crCoord`

- A _Cursor_ specifying the coordinate reference system in which the distance will refer to measure.
- The default value is _None_.

## Return Code

A _List of Double_ specifying the distance between two nodes.

## Sample Code

```psj {3,4,5,6}
Geometry.Part.Cube()

distance = Tools.Measure.Distance.TwoNodes(crNode1=Node(454), 
                                           crNode2=Node(472), 
                                           strTarget="Dist")

JPT.Debugger(distance)

print_str = ", ".join([str(value) for value in distance])
print(print_str)
```
