---
id: Tools-RenumberByConnection
title: Tools.RenumberByConnection()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Renumber by selection
---

## Description

Renumber by selection

## Syntax

```psj
Tools.RenumberByConnection(connectRenumberTool=CONNECT_RENUMBER_TOOL(), crlTargets=[])
```

Ribbon: <menuselection>Tools &#187; RenumberByConnection</menuselection>

## Inputs

### `connectRenumberTool`

- A _CONNECT_RENUMBER_TOOL_ specifying the renumber tool.
- The default value is CONNECT_RENUMBER_TOOL().

### `crlTargets`

- A _List of Cursor_ specifying the target.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.RenumberByConnection(connectRenumberTool=CONNECT_RENUMBER_TOOL(), crlTargets=[])
```
