---
id: JPT-MacroTCursorPairToDItemPair
title: JPT.MacroTCursorPairToDItemPair()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Convert cursor pair (Macro string type) to a pair of DItem object
---

## Description

Convert cursor pair (Macro string type) to a pair of _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object.

## Syntax

```psj
JPT.MacroTCursorPairToDItemPair(cursorPair)
```

## Inputs

### `cursorPair`

- A _String_ specifying the cursor pair (Macro string type).
- This is a required input.

## Return Code

A _[DItemPair](../data-type/psj-utility/pre-utility/built-in-types/DItemPair)_ object.

## Sample Code

```psj {7}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=7730934)
JPT.ViewFitToModel()

# Get all the information of the 2 created cubes
dItemPair = JPT.Debugger(JPT.MacroTCursorPairToDItemPair("3:1-3:2"))
JPT.Debugger(dItemPair.firstDItem)
JPT.Debugger(dItemPair.secondDItem)
```
