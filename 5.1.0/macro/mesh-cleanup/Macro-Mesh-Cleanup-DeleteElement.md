---
id: DeleteElement
title: DeleteElement()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Delete Element

## Syntax

```psj
DeleteElement(cursor[] elemList, bool bKeepShareElem)
```

## Inputs

### `1. Cursor[]`

Target element cursor([11:Element ID])

### `2. Bool`

Keep Share Element bool flag True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
DeleteElement([11:1112], 0)
```
