---
id: Properties-RigidBody
title: Properties.RigidBody()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Assign properties to Rigid Body
---

## Description

Assign a rigid property to a body.

## Syntax

```psj
Properties.RigidBody(...)
```

Ribbon: <menuselection>Properties &#187; Rigid Body</menuselection>

## Inputs

### `strName`

- A _String_ specifying name of the new property.
- The default value is "RigidBody1".

### `iPID`

- An _Integer_ specifying the property identification number.
  This number must be unique with respect to all other property's identification numbers.
- The default value is 1.

### `iRefNodeId`

- An _Integer_ specifying the reference node ID.
- The default value is 0.

### `crlTargets`

- A _List of Cursor_ specifying the entities to be applied the rigid body property.
  The target can be Face entities or Element entities.
- The _crlTargets_ and _crRigidBodyProperty_ arguments are mutually exclusive (one of them must be specified).
- The default value is [].

### `crRigidBodyProperty`

- A _Cursor_ specifying the existing Rigid Body Property.
  - If this argument is not _None_, the specified Rigid Body Property will be modified.
  - Otherwise, a new Rigid Body Property will be created.
- The _crlTargets_ and _crRigidBodyProperty_ arguments are mutually exclusive (one of them must be specified).
- The default value is _None_.

## Return Code

A _Cursor_ specifying the newly created or the modified Rigid Body Property.

## Sample Code

```psj {2}
Geometry.Part.Cube()
Properties.RigidBody(crlTargets=[Face(26)])
```
