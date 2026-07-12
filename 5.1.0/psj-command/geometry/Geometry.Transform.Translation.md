---
id: Geometry-Transform-Translation
title: Geometry.Transform.Translation()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Move the parts along a given vector. The direction and magnitude of the vector are arbitrary or along the specific axis in the Cartesian coordinate system
---

## Description

Move the parts along a given vector. The direction and magnitude of the vector are arbitrary or along the specific axis in the Cartesian coordinate system.

## Syntax

```psj
Geometry.Transform.Translation(...)
```

Macro: [TranslateBody](../../macro/geometry/TranslateBody)

Ribbon: <menuselection>Geometry &#187; Transform &#187; Translation</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the parts to be moved.
- This is a required input.

### `dlTranslationVector`

- A _List of Position_ specifying the translation vector in _crLocalCoordinate_ coordinate system defining the direction and magnitude of the particular translation.
- The default value is [].

### `crLocalCoordinate`

- A _Cursor_ specifying the local coordinate system using for the definition of the _dlTranslationVector_.
- The default value is None.

### `bCreateNewPart`

- A _Boolean_ specifying whether to keep the original parts and create new parts in the moved positions or not.
- The default value is _False_.

### `bCopyLBC`

- A _Boolean_ specifying whether to copy boundary conditions from the existing part to the created parts or not.
- The default value is _False_.

### `bCopyProperty`

- A _Boolean_ specifying whether to copy properties from the existing part to the created parts or not.
- The default value is _False_.

### `bCopyReference`

- A _Boolean_ specifying whether to copy references from the existing part to the created parts or not.
- The default value is _False_.

### `iCopyCount`

- An _Integer_ specifying the number of copies (Creating parts).
- The default value is 1.

## Return Code

A _List of Cursor_ specifying the new parts if success, or _empty_ if fail.

## Sample Code

```psj {2,3}
Geometry.Part.Cube(iPartColor=8124407)
translated_part = Geometry.Transform.Translation(crlParts=[Part(1)],
                                                 dlTranslationVector=[[-0.00666, 0.00222, 0]])
JPT.Debugger(translated_part)
```
