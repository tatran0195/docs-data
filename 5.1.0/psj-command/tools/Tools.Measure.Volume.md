---
id: Tools-Measure-Volume
title: Tools.Measure.Volume()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Measure volume of the specified parts
---

## Description

Measure volume of the specified parts.

## Syntax

```psj
Tools.Measure.Volume(...)
```

Ribbon: <menuselection>Tools &#187; Measure &#187; Volume</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the part to measure volume.
- This is a required input.

### `iPrecision`

- An _Integer_ specifying the number of digit after floating point. The greater `iPrecision` could be, the more accuracy of volume can be measured.
- The default value is 6.

## Return Code

A _Double_ specifying the volume value.

## Sample Code

```psj {3}
Geometry.Part.Cylinder()

volume = Tools.Measure.Volume(crlParts=[Part(1)])

JPT.Debugger(volume)
```
