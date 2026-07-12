---
id: Connections-Contacts-TSSolver-ManualGroup
title: Connections.Contacts.TSSolver.ManualGroup()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Define contact settings between specified groups for TS SunShine solver. Create a group with master and slave surfaces beforehand to define the contact in the contact settings
---

## Description

Define contact settings between specified groups for TS SunShine solver. Create a group with master and slave surfaces beforehand to define the contact in the contact settings.

## Syntax

```psj
Connections.Contacts.TSSolver.ManualGroup(...)
```

Ribbon: <menuselection>Connections &#187; Contacts &#187; TSSolver &#187; ManualGroup</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of the contact to be created.
- The default value is "ContactTSSolver_1".

### `tssolverContact`

- A _list of [TSSOLVER_CONTACT](./../../data-type/psj-command/parameter-types/TSSOLVER_CONTACT)_ specifying the TSSolver contact parameters.
- The default value is [].

### `crplTarget`

- A _List of Cursor Pair_ specifying the list or pair of master face group and slave face group.
- This is a required input.

### `crEdit`

- A _Cursor_ specifying an existing contact settings item:
  - If this parameter is used, the specified contact settings item will be modified. 
  - If it is left _None_, a new contact settings item will be created.
- The default value is _None_.

### `iColor`

- An _Integer_ specifying the contact color.
- The default value is 16711680.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {11,12,13,14,15,16}
Geometry.Part.Cube(iPartColor=12537679)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6250449)

Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_M", 
                        crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_S", 
                        crlTargets=[Face(24)])

created_contact = Connections.Contacts.TSSolver.ManualGroup(strName="ContactTSSolver_2", 
                                                            tssolverContact=TSSOLVER_CONTACT(iIshellelemfaceSlave=0, 
                                                                                             iIshellelemfaceMaster=0), 
                                                            crplTarget=[CursorPair(Group(1), 
                                                                                   Group(2))], 
                                                            iMethod=1)

JPT.Debugger(created_contact)
```
