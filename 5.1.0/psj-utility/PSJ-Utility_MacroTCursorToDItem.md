---
id: JPT-MacroTCursorToDItem
title: JPT.MacroTCursorToDItem()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Convert cursor (Macro string type) to a DItem object
---

## Description

Convert cursor (Macro string type) to a _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object.

## Syntax

```psj
JPT.MacroTCursorToDItem(cursor)
```

## Inputs

### `cursor`

- A _String_ specifying the cursor (Macro string type).
- This is a required input.

## Return Code

A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object.

## Sample Code

```psj {6}
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Convert to DItem and get all the information of the created Cube_1
dItem = JPT.Debugger(JPT.MacroTCursorToDItem("3:1"))
JPT.Debugger(dItem)
```
