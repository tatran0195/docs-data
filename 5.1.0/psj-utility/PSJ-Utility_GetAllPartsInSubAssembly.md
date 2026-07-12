---
id: JPT-GetAllPartsInSubAssembly
title: JPT.GetAllPartsInSubAssembly()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get all the information of all parts under the inputted sub-assembly
---

## Description

Get all the information of all parts under the inputted sub-assembly.

## Syntax

```psj
JPT.GetAllPartsInSubAssembly(subAssem)
```

## Inputs

### `subAssem`

- A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object specifying the inputted sub-assembly.
- This is a required input.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects specifying the parts belonging to the inputted sub-assembly.

## Sample Code

```psj {16}
# Prepare model
Geometry.Part.Cube(iPartColor=15426917)
Geometry.Part.Cube(strName="Cube_2", iPartColor=13390932)
Geometry.Part.Cube(strName="Cube_3", iPartColor=16448103)
Geometry.Part.Cube(strName="Cube_4", iPartColor=13619046)
Geometry.Part.Cube(strName="Cube_5", iPartColor=7861111)
JPT.ViewFitToModel()
Assembly.RightClick.AddSubAssembly()

# Copy all parts to the created Subassembly
currentDoc = JPT.GetActiveDocument()
Assembly.RightClick.TransferDocumentData(strSourceDocTitle=currentDoc.docName, 
                                        strDestDocTitle=currentDoc.docName, 
                                        crlParts=[Part(part.id) for part in JPT.GetAllParts()], 
                                        strlNewPartName=[], 
                                        crDestAssemblyInstance=Inst(1))

# Get the information of all parts belonging to the inputted sub-assembly
listPartsInSubAssembly = JPT.GetAllPartsInSubAssembly(JPT.FindSubAssemblyByID(1))
JPT.Debugger(listPartsInSubAssembly)
```
