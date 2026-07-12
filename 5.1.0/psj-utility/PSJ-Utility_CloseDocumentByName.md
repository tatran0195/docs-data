---
id: JPT-CloseDocumentByName
title: JPT.CloseDocumentByName()
author: TechnoStar Co., Ltd.
description: Close indicated document by using its name.
---

## Description

Close indicated document by using its name.

## Syntax

```psj
JPT.CloseDocumentByName(docName)
```

## Inputs

### `docName`

- A _String_ specifying the name of document to be closed.
- This is a required input.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {4}
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
JPT.CreateNewDocument()
JPT.CloseDocumentByName("101_solid")
```
