---
id: JPT-GetProgramPath
title: JPT.GetProgramPath()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get the path to the current Jupiter installation folder
---

## Description

Get the path to the current Jupiter installation folder.

## Syntax

```psj
JPT.GetProgramPath()
```

## Inputs

This utility function does not require any input value.

## Return Code

The path to the current Jupiter installation folder.

## Sample Code

```psj {2}
# Get the current Jupiter installation folder
path = JPT.GetProgramPath()
JPT.Debugger(path)
```
