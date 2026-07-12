---
id: MeshEdit-CreateNode-Import
title: MeshEdit.CreateNode.Import()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create node by importing CSV file
---

## Description

Create node by importing CSV file.

## Syntax

```psj
MeshEdit.CreateNode.Import(...)
```

Macro: [CreateNodeImport](../../macro/mesh-edit/CreateNodeImport)

Ribbon: <menuselection>MeshEdit &#187; CreateNode &#187; Import</menuselection>

## Inputs

### `strFilePath`

- A _String_ specifying the path of CSV file.
- This is a required input.

## Return Code

- A _List of Cursor_ specifying the created floating nodes.

## Sample Code

```psj {5}
# Put your sample CSV file
csvFile = "C:/temp/NodeData.csv"

# Import nodes
newNode = MeshEdit.CreateNode.Import(strFilePath = csvFile)
JPT.Debugger(newNode) # for checking the return value
```
