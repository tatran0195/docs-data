---
id: JPT-GetCurrentVector
title: JPT.GetCurrentVector()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get all current settings of Vector
---

## Description

Get all current settings of Vector.

## Syntax

```psj
JPT.GetCurrentVector()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _Dictionary_ specifying all settings of the currently displaying Vector.

## Sample Code

```psj {2}
# Get all currently settings of Vector
vectorDict = JPT.GetCurrentVector()

# Dump out result
pprint(vectorDict)

# Print out the Positive color
colorRGB = JPT.ConvertJPTColorToRGB(vectorDict["PositiveColor"])
print("Positive Color: " + colorRGB)
```
