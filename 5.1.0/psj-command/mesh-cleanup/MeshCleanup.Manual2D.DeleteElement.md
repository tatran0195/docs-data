---
id: MeshCleanup-Manual2D-DeleteElement
title: MeshCleanup.Manual2D.DeleteElement()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Delete Element
---

## Description

Delete Element

## Syntax

```psj
MeshCleanup.Manual2D.DeleteElement(crlElems, bKeepShareElem=False)
```

Ribbon: <menuselection>MeshCleanup &#187; Manual2D &#187; DeleteElement</menuselection>

## Inputs

### `crlElems`

- A _List of Cursor_ specifying the element.
- This is a required input.

### `bKeepShareElem`

- A _Boolean_ specifying the keep share element.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual2D.DeleteElement(crlElems, bKeepShareElem=False)
```
