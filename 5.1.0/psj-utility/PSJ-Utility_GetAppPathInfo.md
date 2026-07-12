---
id: JPT-GetAppPathInfo
title: JPT.GetAppPathInfo()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get all the working path of the current Jupiter program
---

## Description

Get all the working path of the current Jupiter program.

## Syntax

```psj
JPT.GetAppPathInfo(PathType)
```

## Inputs

### `PathType`

- An _Enum_ specifying the _[PathType](../data-type/psj-utility/pre-utility/enumeration-types/path-types)_ describing the type of paths which are available for using.
- This is a required input.

## Return Code

A _String_ specifying the path relating to the inputted _[PathType](../data-type/psj-utility/pre-utility/enumeration-types/path-types)_.

## Sample Code

```psj {2}
# Path to the installation folder
print(JPT.GetAppPathInfo(JPT.PathType.PROGRAM_PATH))
```
