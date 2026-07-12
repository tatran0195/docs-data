---
id: JPT-GetCurrentCircle
title: JPT.GetCurrentCircle()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get all current settings of Circle
---

## Description

Get all current settings of Circle.

## Syntax

```psj
JPT.GetCurrentCircle()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _Dictionary_ specifying all settings of the currently displaying Circle.

## Sample Code

```psj {2}
# Get all currently settings of Circle
circleDict = JPT.GetCurrentCircle()

# Dump out result
pprint(circleDict)

# Print out the Highlight color
colorRGB = JPT.ConvertJPTColorToRGB(circleDict["HighlightColor"])
print("Highlight Color: " + colorRGB)
```
