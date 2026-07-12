---
id: Tools-Measure-Area-Element
title: Tools.Measure.Area.Element()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Measure Area By Element
---

## Description

Measure Area By Element

## Syntax

```psj
Tools.Measure.Area.Element(...)
```

Ribbon: <menuselection>Tools &#187; Measure &#187; Area &#187; Element</menuselection>

## Inputs

### `crlElems`

- A _List of Cursor_ specifying the element.
- The default value is [].

### `iPrecision`

- An _Integer_ specifying the precision.
- The default value is 6.

## Return Code

A _Double_ specifying the area value of an element or a total area value of elements.

## Sample Code

```psj {3,6}
Geometry.Part.Cube()

area=Tools.Measure.Area.Element(crlElems=[Elem(1025,1026)])
JPT.Debugger(area)

area=Tools.Measure.Area.Element(crlElems=[Elem(1025,1026)], iPrecision=15)
JPT.Debugger(area)

```
