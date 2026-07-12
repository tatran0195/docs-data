---
id: MeshCleanup-Element-SolidElement
title: MeshCleanup.Element.SolidElement()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Change Topology for Solid Element
---

## Description

Change Topology for Solid Element

## Syntax

```psj
MeshCleanup.Element.SolidElement(crlElems, crPart=None)
```

Ribbon: <menuselection>MeshCleanup &#187; Element &#187; SolidElement</menuselection>

## Inputs

### `crlElems`

- A _List of Cursor_ specifying the element.
- This is a required input.

### `crPart`

- A _Cursor_ specifying the part.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Element.SolidElement(crlElems, crPart=None)
```
