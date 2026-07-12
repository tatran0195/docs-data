---
id: MeshEdit-DividePartByRegion
title: MeshEdit.DividePartByRegion()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Divide Part By Region
---

## Description

Divide Part By Region

## Syntax

```psj
MeshEdit.DividePartByRegion(crlParts=[], crlBoundaryParts=[])
```

Ribbon: <menuselection>MeshEdit &#187; DividePartByRegion</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the part.
- The default value is [].

### `crlBoundaryParts`

- A _List of Cursor_ specifying the boundary parts.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.DividePartByRegion(crlParts=[], crlBoundaryParts=[])
```
