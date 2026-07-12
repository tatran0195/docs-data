---
id: JPT-SetActiveDocumentByName
title: JPT.SetActiveDocumentByName()
author: TechnoStar Co., Ltd.
description: Set indicated document in active by using its name
---

## Description

Set indicated document in active by using its name.

## Syntax

```psj
JPT.SetActiveDocumentByName(docName, BoolType)
```

## Inputs

### `docName`

- A _String_ specifying the name of document to activate.
- This is a required input.

### `BoolType`

- An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the selection mode:
  - _True_: Activate the indicated document.
  - _False_: Do not activate the indicated document.
- This is a required input.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {4}
doc1 = JPT.CreateNewDocument()
doc2 = JPT.CreateNewDocument()
doc3 = JPT.CreateNewDocument()
JPT.SetActiveDocumentByName(doc2.docName,1)
Geometry.Part.Cube()
JPT.ViewFitToModel()
print("Created a Cube in " + str(doc2.docName) + " document")
```
