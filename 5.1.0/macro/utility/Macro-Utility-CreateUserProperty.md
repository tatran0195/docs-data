---
id: CreateUserProperty
title: CreateUserProperty()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Create User Property that stores arbitrary data under Properties item in Assemble Tree.

## Syntax

```psj
CreateUserProperty(string name, string[] properties)
```

## Inputs

### `1. string`

The Name of newly created user property.

### `2. string[]`

The property names inside the newly created user property.


## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateUserProperty("Name", ["data1", "data2", "data3"])
```
