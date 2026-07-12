---
id: CmdOptimizeOuterShellExport
title: CmdOptimizeOuterShellExport()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Export topology optimization surface

## Syntax

```psj

CmdOptimizeOuterShellExport(string fileName, cursor[] parts, float tol)

```
## Inputs
### `1. string  `

Export file name

### `2. cursor[] `

target parts

### `3. float `

Tolerance of density

## Return Code

Nothing.

## Sample Code

```psj
CmdOptimizeOuterShellExport(C:/Temp/export.stl, [3:1], 0.670000)
```
