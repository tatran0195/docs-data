---
id: JPT-GetDocumentList
title: JPT.GetDocumentList()
author: TechnoStar Co., Ltd.
description: Get information of all displaying documents
---

## Description

Get information of all displaying documents.

## Syntax

```psj
JPT.GetDocumentList()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _List of [Document](../data-type/psj-utility/pre-utility/built-in-types/Document)_ object specifying the information of all displaying documents.

## Sample Code

```psj {6}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
JPT.CreateNewDocument()
# Get information of all displaying documents
docList = JPT.GetDocumentList()
for doc in docList:
    JPT.Debugger(doc)
```
