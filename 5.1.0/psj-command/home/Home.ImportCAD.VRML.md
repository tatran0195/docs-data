---
id: Home-ImportCAD-VRML
title: Home.ImportCAD.VRML()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import a Virtual Reality Modeling Language file (*.wrl) to the Jupiter Database
---

## Description

Import a Virtual Reality Modeling Language file (\*.wrl) to the Jupiter Database.

## Syntax

```psj
Home.ImportCAD.VRML(...)
```

Ribbon: <menuselection>Home &#187; ImportCAD &#187; VRML</menuselection>

## Inputs

### `strlPaths`

- A _List of String_ specifying a list of the Virtual Reality Modeling Language files (\*.wrl files) which will be used for importing.
- This is a required input.

### `iVRMLColorGroups`

- An _Integer_ specifying the option that using color information:
  - 0: Do not use
  - 1: Use color information
- The default value is 0.

### `dScale`

- A _Double_ specifying the unit ratio imported from the file's unit into the document's unit.
- The default value is 1.0.

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The Virtual Reality Modeling Language file (\*.wrl file) is imported successfully.
- False: The Virtual Reality Modeling Language file (\*.wrl file) cannot be imported.

## Sample Code

```psj {1,2,3,4}
imported_status = Home.ImportCAD.VRML(strlPaths=[JPT.GetProgramPath() +
                                                 "SampleData/CAD_Model/WRML/GrabCAD 2-SHIP.wrl"],
                                      iVRMLColorGroups=1,
                                      dScale=0.001)
JPT.Debugger(imported_status)
```
