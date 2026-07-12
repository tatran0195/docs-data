---
id: JPT-GetDocumentByName
title: JPT.GetDocumentByName()
author: TechnoStar Co., Ltd.
description: Get information of an indicated document by using its name
---

## Description

Get information of an indicated document by using its name.

## Syntax

```psj
JPT.GetDocumentByName(docName)
```

## Inputs

### `docName`

- A _String_ specifying the name of document to get information.
- This is a required input.

## Return Code

A _[Document](../data-type/psj-utility/pre-utility/built-in-types/Document)_ object specifying the information of document.

## Sample Code

```psj {3}
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
docInfor = JPT.GetDocumentByName("101_solid")
JPT.Debugger(docInfor)
```
