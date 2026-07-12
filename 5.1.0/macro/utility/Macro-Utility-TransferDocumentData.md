---
id: TransferDocumentData
title: TransferDocumentData()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Transfer items in a document to another document.

## Syntax

```psj
TransferDocumentData(string strSourceDocTitle, string strDestDocTitle, cursor[] Parts, string[] strlNewPartName, cursor crDestAssemblyInstance, bool bEnableCutOperation)
```

## Inputs

### `1. String`

The name of source document.

### `2. String`

The name of destination document. 

### `3. cursor[]`

A List of Cursor specifying the transformed parts.

### `4. String[]`

A List of the new names of transformed parts in the destination document.

### `5. Cursor`

The name of destination document. 

### `6. Bool`

Specify cut or copy.
- 0: cut.
- 1: copy.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
TransferDocumentData("Jupiter1", "Jupiter2", [3:1], ["Cube_1"], 0:0, 1)
```
