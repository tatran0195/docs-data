---
id: Connections-Contacts-TSSolver-ManualFace
title: Connections.Contacts.TSSolver.ManualFace()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Define contact settings between specified faces for the TS solver
---

## Description

Define contact settings between specified faces for the TS solver.

## Syntax

```psj
Connections.Contacts.TSSolver.ManualFace(...)
```

Ribbon: <menuselection>Connections &#187; Contacts &#187; TSSolver &#187; ManualFace</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of the contact to be created.
- The default value is "ContactTSSolver_1".

### `tssolverContact`

- A _List of [TSSOLVER_CONTACT](./../../data-type/psj-command/parameter-types/TSSOLVER_CONTACT)_ specifying the TSSolver contact parameters.
- The default value is _[TSSOLVER_CONTACT](./../../data-type/psj-command/parameter-types/TSSOLVER_CONTACT)_.

### `crplTarget`

- A _List of Cursor Pair_ specifying the list or pair of master face group and slave face group.
- This is a required input.

### `crEdit`

- A _Cursor_ specifying an existing contact settings item. 
  - If this parameter is used, the specified contact settings item will be modified. 
  - If it is left _None_, a new contact settings item will be created.
- The default value is _None_.

### `iColor`

- An _Integer_ specifying the contact color.
- The default value is 16711680.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {11,12,13,14}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.015, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6409934)

Tools.Group.CreateGroup(strGroupName="ContactTSSolver_1_Manual_Face_M", 
                        crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="ContactTSSolver_1_Manual_Face_S", 
                        crlTargets=[Face(24)])

created_contact = Connections.Contacts.TSSolver.ManualFace(tssolverContact=TSSOLVER_CONTACT(iIshellelemfaceSlave=0, 
                                                                                            iIshellelemfaceMaster=0), 
                                                           crplTarget=[CursorPair(Group(1), 
                                                                                  Group(2))])

JPT.Debugger(created_contact)
```
