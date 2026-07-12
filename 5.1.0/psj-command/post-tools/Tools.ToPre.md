---
id: Tools-ToPre
title: Tools.ToPre()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Convert the model’s data and the related settings from an opening Post document to a new Pre document. All part names, setting item names and data of setting items in the model are preserved during conversion
---

## Description

Convert the model’s data and the related settings from an opening Post document to a new Pre document. All part names, setting item names and data of setting items in the model are preserved during conversion.

## Syntax

```psj
Tools.ToPre(...)
```

Macro: [ToPre](../../macro/tools/ToPre)

Ribbon: <menuselection>Tools &#187; ToPre</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of Pre document will be converted.
- This is a required input.

### `ilOptions`

- A _List of Integer_ specifying the related settings will be converted with model.
    - 0: Group
    - 1: LBC
    - 2: Connection
    - 3: Coordinate
    - 4: Property
- The default value is [].

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {6}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\Post\\Static_Renkon.op2"
Home.ImportResults.Nastran(strPath= samplePath, dFaceAngle=60.16, dEdgeAngle=60.16, bReadLoadAndConstraint=True, 
                            bReadConnection=True, bCreateResultsAtMidNode=True)
# Convert to Pre
data = Tools.ToPre(strName="Static_Renkon", ilOptions=[0, 1, 2, 3, 4])
JPT.SetActiveDocumentByName("Static_Renkon",1)
JPT.Debugger(data)
```
