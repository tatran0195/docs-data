---
id: Analysis-ACTRAN-Run
title: Analysis.ACTRAN.Run()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Run Actran analysis
---

## Description

Run Actran analysis

## Syntax

```psj
Analysis.ACTRAN.Run(...)
```

Ribbon: <menuselection>Analysis &#187; ACTRAN &#187; Run</menuselection>

## Inputs

### `actranAnalysis`

- A _[ACTRAN_ANALYSIS](./../../data-type/psj-command/parameter-types/ACTRAN_ANALYSIS)_ specifying the Actran analysis data structure.
- The default value is _[ACTRAN_ANALYSIS](./../../data-type/psj-command/parameter-types/ACTRAN_ANALYSIS)_.

### `crlTargets`

- A _List of Cursor_ specifying the target.
- The default value is [].

### `crEdit`

- A _Cursor_ specifying the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.ACTRAN.Run(actranAnalysis=ACTRAN_ANALYSIS(), crlTargets=[], crEdit=None)
```
