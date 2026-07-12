---
id: Geometry-ShowAdjacent-Elements
title: Geometry.ShowAdjacent.Elements()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Expand the selection in all directions, regardless of the shape of surrounding features or the angle at which objects are joined. It obtained by recursively finding adjacent elements at an angle of less than or equal to the specified angle
---

## Description

Expand the selection in all directions, regardless of the shape of surrounding features or the angle at which objects are joined.
It obtained by recursively finding adjacent elements at an angle of less than or equal to the specified angle.

## Syntax

```psj
Geometry.ShowAdjacent.Elements(...)
```

Ribbon: <menuselection>Geometry &#187; Show Adjacent &#187; Elements</menuselection>

## Inputs

### `dAngle`

- A _Double_ specifying the angle between elements in degree. The adjacent elements that are at an angle of less than or equal to _dAngle_ will be selected.
- The default value is 0.0.

### `bIncludeStopElems`

- A _Boolean_ specifying whether to add the stop elements to the selection list or not.
- The default value is _False_.

### `iNumOfLayers`

- An _Integer_ specifying the number of adjacent layers to be searched.
- The default value is 1.

### `crlStartElems`

- A _List of Cursor_ specifying a sequence of the start elements.
- The default value is [].

### `crlStopElems`

- A _List of Cursor_ specifying a sequence of the stop elements.
- The default value is [].

## Return Code

A _List of Cursor_ specifying a sequence of adjacent elements.

## Sample Code

```psj {2}
Geometry.Part.Cube()
adjacent_elements = Geometry.ShowAdjacent.Elements(dAngle=5.0, crlStartElems=[Elem(1005)])
JPT.Debugger(adjacent_elements)
```
