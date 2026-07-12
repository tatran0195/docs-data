---
id: JPT-GetCurrentDocumentPath
title: JPT.GetCurrentDocumentPath()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get the path of the current working Jupiter file
---

## Description

Get the path of the current working Jupiter file.

## Syntax

```psj
JPT.GetCurrentDocumentPath()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _String_ specifying the full path to the current Jupiter file.

## Sample Code

```psj {2}
# Open an existing Jupiter file (*.jtdb) or (*.jth5) before running the below code
path = JPT.GetCurrentDocumentPath()
print(path)
```
