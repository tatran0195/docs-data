---
id: JPT-GetCurrentDeformation
title: JPT.GetCurrentDeformation()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get all current settings of Deformation
---

## Description

Get all current settings of Deformation.

## Syntax

```psj
JPT.GetCurrentDeformation()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _Dictionary_ specifying all settings of the currently displaying Deformation.

## Sample Code

```psj {2}
# Get all currently settings of Deformation
deformDict = JPT.GetCurrentDeformation()

# Dump out result
pprint(deformDict)

# Print out the Edge color
colorRGB = JPT.ConvertJPTColorToRGB(deformDict["EdgeColor"])
print("Edge Color: " + colorRGB)
```
