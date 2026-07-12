---
id: MidPlaneEdit-Manual-vecOffset
title: MidPlaneEdit.Manual.vecOffset()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Unknown Description
---

## Description

Unknown Description

## Syntax

```psj
MidPlaneEdit.Manual.vecOffset(crlFaces, crPart, dOffset, bCyl, strNewPartName)
```

Ribbon: <menuselection>MidPlaneEdit &#187; Manual &#187; vecOffset</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying the face.
- This is a required input.

### `crPart`

- A _Cursor_ specifying the part.
- This is a required input.

### `dOffset`

- A _Double_ specifying the offset.
- This is a required input.

### `bCyl`

- A _Boolean_ specifying the cylinder.
- This is a required input.

### `strNewPartName`

- A _String_ specifying the new part name.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.Manual.vecOffset(crlFaces, crPart, dOffset, bCyl, strNewPartName)
```
