---
id: MaterialInfo
title: MaterialInfo()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Get the information in the materials

## Syntax

```psj
MaterialInfo(String MatName,String Info Type)
```

## Inputs

### `1. String`

Material Name

### `2. String`

Info Type (DENSITY or YOUNGMODULUES or POISSONRATIO)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MaterialInfo("Structural_Steel","DENSITY")
```

or

```psj
MaterialInfo("Structural_Steel","YOUNGMODULUES")
```
