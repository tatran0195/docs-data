---
id: JPT-MessageBoxPSJ
title: JPT.MessageBoxPSJ()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Show a Jupiter dialog (Information, Warning)
---

## Description

Show a Jupiter dialog (Information, Warning).

## Syntax

```psj
JPT.MessageBoxPSJ(messageContent, messageBoxType)
```

## Inputs

### `messageContent`

- A _String_ specifying the message which will be shown on the created message box.
- This is a required input.

### `messageBoxType`

- An _Enum_ specifying the _[MsgBoxType](../data-type/psj-utility/pre-utility/enumeration-types/msgbox-types)_ describing the type of creating message box in Jupiter.
- This is a required input.

## Return Code

The selected option (YES, NO, OK, CANCEL).

## Sample Code

```psj {2}
# Show an information message box
returnValue = JPT.MessageBoxPSJ("Test dialog",JPT.MsgBoxType.MB_INFORMATION_OK)
JPT.Debugger(returnValue) # Return a string object with value = OK
```
