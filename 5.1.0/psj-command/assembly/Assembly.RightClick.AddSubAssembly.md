---
id: Assembly-RightClick-AddSubAssembly
title: Assembly.RightClick.AddSubAssembly()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Add a new assembly (Sub-assembly) to the selected assembly
---

## Description

Add a new assembly (Sub-assembly) to the selected assembly.

## Syntax

```psj
Assembly.RightClick.AddSubAssembly(...)
```

Ribbon: <menuselection>Assembly &#187; Right Click &#187; Add Subassembly</menuselection>

## Inputs

### `crInst`

- A _Cursor_ specifying the instance inwhich the new subassembly will be added.
- The default value is None.

## Return Code

A _Cursor_ specifying the created sub-assembly.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

Assembly.RightClick.AddSubAssembly()
created_sub_assem = Assembly.RightClick.AddSubAssembly(crInst=Inst(1))

JPT.Debugger(created_sub_assem)
```
