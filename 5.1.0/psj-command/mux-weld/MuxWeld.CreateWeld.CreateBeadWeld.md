---
id: MuxWeld-CreateWeld-CreateBeadWeld
title: MuxWeld.CreateWeld.CreateBeadWeld()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a bead weld.
---

## Description

Create a bead weld.

## Syntax

```psj
MuxWeld.CreateWeld.CreateBeadWeld(crlEdges, crlPrjtedEdge, crlParts, dTol, dRatio, crRefElem)
```

Ribbon: <menuselection>MuxWeld &#187; CreateWeld &#187; CreateBeadWeld</menuselection>

## Inputs

### `crlEdges`

- A _List of Cursor_ specifying the edge.
- This is a required input.

### `crlPrjtedEdge`

- A _List of Cursor_ specifying the projected edge.
- This is a required input.

### `crlParts`

- A _List of Cursor_ specifying the part.
- This is a required input.

### `dTol`

- A _Double_ specifying the tolerance.
- This is a required input.

### `dRatio`

- A _Double_ specifying the ratio.
- This is a required input.

### `crRefElem`

- A _Cursor_ specifying the reference element.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MuxWeld.CreateWeld.CreateBeadWeld(crlEdges, crlPrjtedEdge, crlParts, dTol, dRatio, crRefElem)
```
