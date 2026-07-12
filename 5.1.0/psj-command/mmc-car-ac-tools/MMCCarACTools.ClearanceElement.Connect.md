---
id: MMCCarACTools-ClearanceElement-Connect
title: MMCCarACTools.ClearanceElement.Connect()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: MMCCarACTools ClearanceElement Connect
---

## Description

MMCCarACTools ClearanceElement Connect

## Syntax

```psj
MMCCarACTools.ClearanceElement.Connect(crlFaces, crlElems, iConnectionMethod)
```

Ribbon: <menuselection>MMCCarACTools &#187; ClearanceElement &#187; Connect</menuselection>

## Inputs

### `crlFaces`

- A _List of Cursor_ specifying the face.
- This is a required input.

### `crlElems`

- A _List of Cursor_ specifying the element.
- This is a required input.

### `iConnectionMethod`

- An _Integer_ specifying the connection method.
- This is a required input.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MMCCarACTools.ClearanceElement.Connect(crlFaces, crlElems, iConnectionMethod)
```
