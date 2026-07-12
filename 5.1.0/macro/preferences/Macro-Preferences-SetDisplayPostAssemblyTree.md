---
id: SetDisplayPostAssemblyTree
title: SetDisplayPostAssemblyTree()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Enalble/disable calculating the Tresca Stress automatically when the result file is opened.

## Syntax

```psj
SetDisplayPostAssemblyTree(bool UseTrescaStress)
```

## Inputs

### `1. bool`

- "1": Enable saving load with Tresca Stress calculation
- "0": Disable saving load with Tresca Stress calculation

## Return Code

No return code.

## Sample Code

```psj
SetDisplayPostAssemblyTree(0)
```
