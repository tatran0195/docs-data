---
id: Home-ImportResults-MuxWeld
title: Home.ImportResults.MuxWeld()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import Mux-Weld result file. 
---

## Description

Import Mux-Weld result file. 

## Syntax

```psj
Home.ImportResults.MuxWeld(...)
```

Macro: [ImportMuxWeld](../../macro/home/ImportMuxWeld)

Ribbon: <menuselection>Home &#187; ImportResults &#187; MuxWeld</menuselection>

## Inputs

### `strPath`

- A _String_ specifying Mux-Weld result file path.
- This is a required input.

### `iImportType`

- An _Integer_ specifying import type. For LS-Dyna, it is always set to 1. 
- The default value is 1.

### `dFaceAngle`

- A _Double_ specifying the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).
- The default value is 60.0 (degree).

### `dEdgeAngle`

- A _Double_ specifying the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).
- The default value is 60.0 (degree).

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The MuxWeld result is imported successfully.
- False: The MuxWeld result cannot be imported.

## Sample Code

```psj {4}
#Please set path to your sample mux-weld file.
filepath="C:/Temp/Sample.wsi"

Home.ImportResults.MuxWeld(filepath)
```
