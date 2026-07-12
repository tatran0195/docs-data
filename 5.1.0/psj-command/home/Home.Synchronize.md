---
id: Home-Synchronize
title: Home.Synchronize()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Enable/Disable the synchronize function between documents
---

## Description

Enable/Disable the synchronize function between documents.

## Syntax

```psj
Home.Synchronize(...)
```

Ribbon: <menuselection>Home &#187; Synchronize</menuselection>

## Inputs

This function does not contain any input values.

## Return Code

A _Boolean_ specifying the status of the process:

- _True_: The windows are synchronized.
- _False_: Synchronizing mode is disabled.

## Sample Code

```psj {1}
synchronize = Home.Synchronize()

JPT.Debugger(synchronize)
```
