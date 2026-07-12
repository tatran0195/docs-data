---
id: JPT-GetDictMatPropKeys
title: JPT.GetDictMatPropKeys()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get list keys from dictMatProps
---

## Description

Get list keys from dictMatProps.

## Syntax

```psj
JPT.GetDictMatPropKeys(dictMatProps)
```

## Inputs

### `dictMatProps`

- A _Dictionary_ specifying the _[dictMatProps](../data-type/psj-utility/pre-utility/built-in-types/DMaterial)_.
- This is a required input.

## Return Code

A _List of String_ specifying the keys of dictMatProps.

## Sample Code

```psj {11}
# Get 1st material in the library materials
mat0 = JPT.GetAllLibraryMaterials()[0]

# Get & print dicMatProps
dict1 = mat0.dictMatProps
pprint(dict1)
```
