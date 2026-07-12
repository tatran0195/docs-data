---
id: Home-AddResults-UsersResult
title: Home.AddResults.UsersResult()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Add user result to the current Jupiter Database. 
---

## Description

Add user result to the current Jupiter Database. 

## Syntax

```psj
Home.AddResults.UsersResult(...)
```

Macro: [AddUserResultDefine](../../macro/home/AddUserResultDefine)

Ribbon: <menuselection>Home &#187; AddResults &#187; UsersResult</menuselection>

## Inputs

### `strlPath`

- A _List of String_ specifying user result files.
- This is a required input.

### `bExportLog`

-A _Boolean_ specifying whether or not 
- The default value is _False_.

## Return Code

- A _Boolean_ specifying whether or not the function is executed successfully or not:
  - True: The user result is added to the document successfully.
  - False: The user result is not added to the document.

## Sample Code

```psj {8}
# Put your sample files
mesh = "C:/Temp/mesh.bdf"
result = "C:/Temp/result.csv"

# Import mesh file
Home.ImportResults.ImportMesh.Nastran(mesh)
# Add result to the mesh file.
Home.AddResults.UsersResult(strlPath=result)
```
