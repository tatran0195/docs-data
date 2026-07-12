---
id: JPT-GetCurrentAnimation
title: JPT.GetCurrentAnimation()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get all current settings of Animation
---

## Description

Get all current settings of Animation.

## Syntax

```psj
JPT.GetCurrentAnimation()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _Dictionary_ specifying all current settings of Animation.

## Sample Code

```psj {2}
# Get all currently settings of Animation
animationDict = JPT.GetCurrentAnimation()

# Dump out result
pprint(animationDict)

# Print out the Frame number
print("Frame Number: " + str(animationDict["FrameNumber"]))
```
