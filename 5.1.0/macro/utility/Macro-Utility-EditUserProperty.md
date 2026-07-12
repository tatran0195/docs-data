---
id: EditUserProperty
title: EditUserProperty()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Edit existing User Property in Assemble Tree.

## Syntax

```psj
EditUserProperty(string name, string[] values)
```

## Inputs

### `1. string`

The Name of user property to edit.

### `2. string[]`

The values corresponding to the properties  inside the newly created user property.


## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
EditUserProperty("Name", ["1.0", "2.0", "3.0"])
```
