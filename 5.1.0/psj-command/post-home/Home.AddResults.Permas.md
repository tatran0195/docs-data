---
id: Home-AddResults-Permas
title: Home.AddResults.Permas()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Add permas result to the current Jupiter Database. 
---

## Description

Add permas result to the current Jupiter Database. 

## Syntax

```psj
Home.AddResults.Permas(...)
```

Macro: [AddResultsPermas](../../macro/home/AddResultsPermas)

Ribbon: <menuselection>Home &#187; AddResults &#187; Permas</menuselection>

## Inputs

### `strlPaths`

- A _List of String_ specifying permas result files.
- This is a required input.

### `bMergeTree`

- A _Boolean_ specifying whether or not the differences not included in the existing document will be added.
- The default value is _True_.

## Return Code

- A _Boolean_ specifying whether or not the function is executed successfully or not:
  - True: The permas result is added to the document successfully.
  - False: The permas result is not added to the document.

## Sample Code

```psj {8}
# Put your sample files
mesh = "C:/Temp/mesh.dat"
result = "C:/Temp/result.post.gz"

# Import mesh file
Home.ImportResults.Permas(mesh)
# Add result to the mesh file.
Home.AddResults.Permas(strlPaths=[result], bMergeTree=False)
```
