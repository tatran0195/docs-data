---
id: GetUserProperty
title: GetUserProperty()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Get a value of User Property.

## Syntax

```psj
CreateUserProperty(string name, string[] properties)
```

## Inputs

### `1. string`

The Name of newly created user property.

### `2. int`

The ID of the data.


## Return Code

- The value corresponding to the ID of the data.

## Sample Code

```psj
# Create a new user property
JPT.Exec(f'CreateUserProperty("Name", ["data1", "data2", "data3"])')

# Add values to the created user property
JPT.Exec(f'EditUserProperty("Name", ["1.0", "2.0", "3.0"])')

# Get 1st value of the specified user property
value=JPT.Exec(f'GetUserProperty("Name", 1)')
print(value)
```
