---
id: MeshCleanup-Manual2D-MergeElement-TwoQuadsToQuad
title: MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Merge two Quad elements into one Quad element
---

## Description

Merge two Quad elements into one Quad element

## Syntax

```psj
MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad(crlElems)
```

Ribbon: <menuselection>MeshCleanup &#187; Manual2D &#187; MergeElement &#187; TwoQuadsToQuad</menuselection>

## Inputs

### `crlElems`

- A _List of Cursor_ specifying the element.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad(crlElems)
```
