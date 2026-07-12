---
id: Assembly-RightClick-TransferDocumentData
title: Assembly.RightClick.TransferDocumentData()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Transfer data information of entity between documents
---

## Description

Transfer data information of entity between documents.

## Syntax

```psj
Assembly.RightClick.TransferDocumentData(...)
```

Macro: [TransferDocumentData](../../macro/utility/TransferDocumentData)

Ribbon: <menuselection>Assembly &#187; Right Click &#187; Copy</menuselection>

## Inputs

### `strSourceDocTitle`

- A _String_ specifying the name of source document.
- The is the required input.

### `strDestDocTitle`

- A _String_ specifying the name of destination document. If the destination document does not exist before running this PSJ-Command, it will firsly create a new document with the name used in `strDestDocTitle`
- The is the required input.

### `crlParts`

- A _List of Cursor_ specifying the transformed parts.
- The is the required input.

### `strlNewPartName`

- A _List of String_ specifying the new name of transformed parts in the destination document.
- The default value is [].

### `crDestAssemblyInstance`
- A _Cursor_ specifying the sub assembly where transformed parts moves.

### `bEnableCutOperation`

- A _Boolean_ specifying cut or paste.
- False: cut, True: copy.

## Return Code

A _Cursor_ specifying the newly created parts in destination document.

:::note
PSJ interpreter will raise error (exception) when it can not find an entity in database (a database query error). With a wrong input argument (document name, part ID) then it can lead to a query error rather than return a failed result.
:::

## Sample Code

```psj {9-13}
# Create a Cube in 1st document.
doc1=JPT.GetActiveDocument()
Geometry.Part.Cube()

#2nd doc is created
doc2=JPT.CreateNewDocument()

# Copy/Transfer Cube into document 2: 
result = Assembly.RightClick.TransferDocumentData(
    strSourceDocTitle=doc1.docName, 
    strDestDocTitle=doc2.docName,
    crlParts=[Part(1)], 
    strlNewPartName=[])

# Check cube in both 1st and 2nd document.
Home.Windows.TileVertical(iMode=1)
Home.Synchronize()
JPT.ViewFitToModel()
```
