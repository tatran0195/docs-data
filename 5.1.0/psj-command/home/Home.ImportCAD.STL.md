---
id: Home-ImportCAD-STL
title: Home.ImportCAD.STL()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import a Standard Tessellation Language file (*.stl) to the Jupiter Database
---

## Description

Import a Standard Tessellation Language file (\*.stl) to the Jupiter Database.

## Syntax

```psj
Home.ImportCAD.STL(...)
```

Ribbon: <menuselection>Home &#187; ImportCAD &#187; STL</menuselection>

## Inputs

### `strlPath`

- A _List of String_ specifying a list of the Standard Tessellation Language files (\*.stl files) which will be used for importing.
- This is the required input.

### `dScale`

- A _Double_ specifying the unit ratio imported from the file's unit into the document's unit.
- The default value is 0.001.

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The Standard Tessellation Language file (\*.stl file) is imported successfully.
- False: The Standard Tessellation Language file (\*.stl file) cannot be imported.

## Sample Code

```psj {1,2,3}
imported_status = Home.ImportCAD.STL(strlPaths=[JPT.GetProgramPath() +
                                                "SampleData/CAD_Model/STL/Macbook Pro 15.stl"],
                                     dScale=0.001)
JPT.Debugger(imported_status)
```
