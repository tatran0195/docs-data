---
id: CmdAddResultTSVPost
title: CmdAddResultTSVPost()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Add result to current mesh data.

## Syntax

```psj
CmdAddResultTSVPost(cursor Job, string[] path, int solverType, int offsetID)
```
## Inputs

### `1. cursor `

Post job.

### `2. string[] `

File paths.

### `3. int `

_[Solver type](../../data-type/psj-utility/post-utility/enumeration-types/post-job-type.md)_.

#### `4. int `

Offset ID.

## Return Code

Nothing.

## Sample Code

```psj
CmdAddResultTSVPost(183:1, ["C:/temp/data.unv"], 4, 1)
```
