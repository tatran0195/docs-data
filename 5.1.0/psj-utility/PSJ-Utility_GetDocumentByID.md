---
id: JPT-GetDocumentByID
title: JPT.GetDocumentByID()
author: TechnoStar Co., Ltd.
description: Get information of an indicated document by using its ID
---

## Description

Get information of an indicated document by using its ID.

## Syntax

```psj
JPT.GetDocumentByID(docID)
```

## Inputs

### `docID`

- A _String_ specifying the ID of document to get information.
- This is a required input.

## Return Code

A _[Document](../data-type/psj-utility/pre-utility/built-in-types/Document)_ object specifying the information of document.

## Sample Code

```psj {2}
doc = JPT.CreateNewDocument()
docInfor = JPT.GetDocumentByID(doc.docID)
JPT.Debugger(docInfor)
```
