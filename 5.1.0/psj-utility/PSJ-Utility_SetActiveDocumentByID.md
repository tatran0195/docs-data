---
id: JPT-SetActiveDocumentByID
title: JPT.SetActiveDocumentByID()
author: TechnoStar Co., Ltd.
description: Set indicated document in active by using its ID
---

## Description

Set indicated document in active by using its ID.

## Syntax

```psj
JPT.SetActiveDocumentByID(docID, BoolType)
```

## Inputs

### `docID`

- A _String_ specifying the ID of document to activate.
- This is a required input.

### `BoolType`

- An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the selection mode:
  - _True_: Activate the indicated document.
  - _False_: Do not activate the indicated document.
- This is a required input.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {3}
doc1 = JPT.CreateNewDocument()
doc2 = JPT.CreateNewDocument()
JPT.SetActiveDocumentByID(doc1.docID, 1)
Geometry.Part.Cube()
JPT.ViewFitToModel()
```
