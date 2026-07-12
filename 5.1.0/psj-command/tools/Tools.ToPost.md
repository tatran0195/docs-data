---
id: Tools-ToPost
title: Tools.ToPost()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Convert the model's data and from an opening Pre document to a new Post document enables to add result to the model.
---

## Description

Convert the model's data and from an opening Pre document to a new Post document enables to add result to the model.

## Syntax

```psj
Tools.ToPost(...)
```

Macro: 

Ribbon: <menuselection>Tools &#187; ToPost</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of Post document will be converted.
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

```psj {5}
# Prepare Pre model
Geometry.Part.Cube()

# Convert to Post
Tools.ToPost(strName="Jupiter1", ilOptions=[0, 1, 2, 3, 4])
```
