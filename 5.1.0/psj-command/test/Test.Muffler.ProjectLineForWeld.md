---
id: Test-Muffler-ProjectLineForWeld
title: Test.Muffler.ProjectLineForWeld()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Projec line for weld
---

## Description

Projec line for weld

## Syntax

```psj
Test.Muffler.ProjectLineForWeld(crlEdges, crlFaces)
```

Ribbon: <menuselection>Test &#187; Muffler &#187; ProjectLineForWeld</menuselection>

## Inputs

### `crlEdges`

- A _List of Cursor_ specifying the edge.
- This is a required input.

### `crlFaces`

- A _List of Cursor_ specifying the face.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.Muffler.ProjectLineForWeld(crlEdges, crlFaces)
```
