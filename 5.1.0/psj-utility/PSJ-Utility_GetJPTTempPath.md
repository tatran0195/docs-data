---
id: JPT-GetJPTTempPath
title: JPT.GetJPTTempPath()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get the path to the temporary folder of the current Jupiter program
---

## Description

Get the path to the temporary folder of the current Jupiter program.

## Syntax

```psj
JPT.GetJPTTempPath()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _String_ specifying the path to the current Jupiter temporary folder.

## Sample Code

```psj {2}
# Get the current Jupiter temporary folder
path = JPT.GetJPTTempPath()
JPT.Debugger(path)
```
