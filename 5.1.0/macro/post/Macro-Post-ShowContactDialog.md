---
id: ShowContactDialog
title: ShowContactDialog()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Show contact dialog.

## Syntax

```psj
ShowContactDialog(int iResultSet, int iTimeStep, string strResultTypeName, string strResultCompName, int iResultPosition)
```

## Inputs

### `1. int `

Result set.

### `2. int `

Time step.

### `3. string `

Name of result type.

### `4. string `

Name of component.

### `5. int `

Data Location.

## Return Code

Nothing.

## Sample Code

```psj
ShowContactDialog(1, 0, 0, ContactForceShear, Translational, 1)
```
