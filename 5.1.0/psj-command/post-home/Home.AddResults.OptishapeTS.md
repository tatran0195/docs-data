---
id: Home-AddResults-OptishapeTS
title: Home.AddResults.OptishapeTS()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Add Optishape-TS results to the current Jupiter Database. 
---

## Description

Add Optishape-TS results to the current Jupiter Database. 

## Syntax

```psj
Home.AddResults.OptishapeTS(...)
```

Macro: [AddResultsOptishapeTS](../../macro/home/AddResultsOptishapeTS)

Ribbon: <menuselection>Home &#187; AddResults &#187; OptishapeTS</menuselection>

## Inputs

### `strlPaths`

- A _List of String_ specifying a list of the Optishape-TS files (\*.op2 files)
- This is a required input.

### `bMergeTree`

- A _Boolean_ specifying whether or not the differences not included in the existing document will be added.
- The default value is _True_.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Optishape-TS result is added to the document successfully.
  - False: The Optishape-TS result is not added to the document.

## Sample Code

```psj {8}
# Put your sample files
Result1 = "C:/Temp/topo.op2"
Result2 = "C:/Temp/topo_result.op2"

Home.ImportResults.OptishapeTS(strlPaths=[Result1])
Home.AddResults.OptishapeTS(strlPaths=[Result2])
```
