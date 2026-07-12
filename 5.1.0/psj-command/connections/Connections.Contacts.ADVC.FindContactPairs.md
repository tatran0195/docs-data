---
id: Connections-Contacts-ADVC-FindContactPairs
title: Connections.Contacts.ADVC.FindContactPairs()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Find contact pairs.
---

## Description

Find contact pairs.

## Syntax

```psj
Connections.Contacts.ADVC.FindContactPairs(...)
```

Ribbon: <menuselection>Connections &#187; Contacts &#187; ADVC &#187; FindContact</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the target parts.
- This is the required input.

### `dFindTolerance`

- A _Double_ specifying tolerance to find contact.
- The default value is 0.0002.

### `dTolForTIED`

- A _Double_ specifying the distance to set tied.
- The default value is 0.1.

## Return Code

A _stAdvcParam_ specifying the parameters of contacts.

## Sample Code

```psj {12-15}
Geometry.Part.Cube(
  iPartColor=6409934)
Geometry.Part.Cube(
  dlOrigin=[0.01, 0.0, 0.0], 
  strName="Cube_2", 
  iPartColor=7463537)
Geometry.Part.Cube(
  dlOrigin=[0.02, 0.0, 0.0], 
  strName="Cube_3", 
  iPartColor=7666683)

cont=Connections.Contacts.ADVC.FindContactPairs(
    crlParts=[Part(1, 2, 3)], 
    dFindTolerance=0.0002, 
    dTolForTIED=0.1)

for c in cont:
    c.stAdvcParam.dClearance=0.1234

Connections.Contacts.ADVC.ContactTable_Advc(cont)
```
