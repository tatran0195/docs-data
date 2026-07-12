---
id: CloseGaps
title: CloseGaps()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Close small Gaps

## Syntax

```psj
CloseGaps(cursor[] taBodyCur, double dDistanceTol)
```

## Inputs

### `1. Cursor[]`

Target part cursor([3:Part ID])

### `2. Double`

Close gap distance tolerance

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CloseGaps([3:1], 0.0001)
```
