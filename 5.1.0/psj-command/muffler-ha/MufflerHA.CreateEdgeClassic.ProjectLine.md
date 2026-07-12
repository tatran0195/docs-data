---
id: MufflerHA-CreateEdgeClassic-ProjectLine
title: MufflerHA.CreateEdgeClassic.ProjectLine()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: create edge
---

## Description

Create edge

## Syntax

```psj
MufflerHA.CreateEdgeClassic.ProjectLine(ilAiedgeidForMacro, ilAifaceidForMacro, bDivideFace, crlAiparttargetForMarco)
```

Ribbon: <menuselection>MufflerHA &#187; CreateEdgeClassic &#187; ProjectLine</menuselection>

## Inputs

### `ilAiedgeidForMacro`

- A _List of Integer_ specifying the aiedgeid for macro.
- This is a required input.

### `ilAifaceidForMacro`

- A _List of Integer_ specifying the aifaceid for macro.
- This is a required input.

### `bDivideFace`

- A _Boolean_ specifying the divide face.
- This is a required input.

### `crlAiparttargetForMarco`

- A _List of Cursor_ specifying the part target for marco.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MufflerHA.CreateEdgeClassic.ProjectLine(ilAiedgeidForMacro, ilAifaceidForMacro, bDivideFace, crlAiparttargetForMarco)
```
