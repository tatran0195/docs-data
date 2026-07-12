---
id: FindFacesInPart
title: FindFacesInPart()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Find Faces in a Part.

## Syntax

```psj
FindFacesInPart(Cursor crTargetPart, string strTargetPartString)
```

## Inputs

### `1. Cursor`

Target part cursor (3:Part ID)

### `2. String`

Finding Target(MaxXFACE,MinXFACE,MaxYFACE,MinYFACE,MaxZFACE,MinZFACE)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
JPT.Exec('FindFacesInPart(3:3, "MaxZFACE")')
```
