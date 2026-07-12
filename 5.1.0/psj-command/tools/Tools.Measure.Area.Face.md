---
id: Tools-Measure-Area-Face
title: Tools.Measure.Area.Face()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Measure an area of a face or a total area of faces
---

## Description

Measure an area of a face or a total area of faces.

## Syntax

```psj
Tools.Measure.Area.Face(...)
```

Ribbon: <menuselection>Tools &#187; Measure &#187; Area &#187; Face</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying the list of faces to measure area.
- This is a required input.

### `iPrecision`

- An _Integer_ specifying the number of digit after floating point. The greater `iPrecision` could be, the more accuracy of Area can be measured.
- The default value is 6.

## Return Code

A _Double_ specifying the area value of a face or a total area value of faces.

## Sample Code

```psj {3}
Geometry.Part.Cube()

area = Tools.Measure.Area.Face(crlFaces=[Face(26)])

JPT.Debugger(area)
```
