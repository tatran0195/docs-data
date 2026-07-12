---
id: Test-Connection-RRod
title: Test.Connection.RRod()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: create RRod
---

## Description

Create RRod

## Syntax

```psj
Test.Connection.RRod(rbarConnection=RBAR_CONNECTION(), iUlDOFs=1, dTol=0.0, crlMasterTargets=[], crlSlaveTargets=[])
```

Ribbon: <menuselection>Test &#187; Connection &#187; RRod</menuselection>

## Inputs

### `rbarConnection`

- A _RBAR_CONNECTION_ specifying the connection.
- The default value is RBAR_CONNECTION().

### `iUlDOFs`

- An _Integer_ specifying the ul d o fs.
- The default value is 1.

### `dTol`

- A _Double_ specifying the tolerance.
- The default value is 0.0.

### `crlMasterTargets`

- A _List of Cursor_ specifying the master target.
- The default value is [].

### `crlSlaveTargets`

- A _List of Cursor_ specifying the slave target.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.Connection.RRod(rbarConnection=RBAR_CONNECTION(), iUlDOFs=1, dTol=0.0, crlMasterTargets=[], crlSlaveTargets=[])
```
