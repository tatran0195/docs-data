---
id: CmdPostPPTMultiShots
title: CmdPostPPTMultiShots()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Create ppt of modal analysis.

## Syntax

```psj
CmdPostPPTMultiShots(dStartFrequency, dEndFrequency)
```

## Inputs

### `1. double `

Start Frequency.

### `2.double `

End Frequency.

## Return Code

- "1": The function can be executed.
- "0": The function cannot be executed.

## Sample Code

```psj
CmdPostPPTMultiShots(0.000000, 1000.000000)
```
