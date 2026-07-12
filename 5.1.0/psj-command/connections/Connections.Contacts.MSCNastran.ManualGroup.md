---
id: Connections-Contacts-MSCNastran-ManualGroup
title: Connections.Contacts.MSCNastran.ManualGroup()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Define contact settings between specified groups for MSC Nastran solver. Create a group with master and slave surfaces beforehand to define the contact in the contact settings
---

## Description

Define contact settings between specified groups for MSC Nastran solver. Create a group with master and slave surfaces beforehand to define the contact in the contact settings.

## Syntax

```psj
Connections.Contacts.MSCNastran.ManualGroup(...)
```

Macro: [ContactMSCNastran](../../macro/connections/ContactMSCNastran)

Ribbon: <menuselection>Connections &#187; Contacts &#187; MSCNastran &#187; ManualGroup</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name of the contact to be created.
- The default value is "ContactMSCNastran_1".

### `nastranContact`

- A _[NASTRAN_CONTACT](./../../data-type/psj-command/parameter-types/NASTRAN_CONTACT)_ specifying the Nastran contact parameters.
- The default value is _[NASTRAN_CONTACT](./../../data-type/psj-command/parameter-types/NASTRAN_CONTACT)_.

### `crplTarget`

- A _Cursor Pair List_ specifying the list or pair of master face group and slave face group.
- This is a required input.

### `crEdit`

- A _Cursor_ specifying an existing contact settings item. 
  - If this parameter is used, the specified contact settings item will be modified. 
  - If it is left _None_, a new contact settings item will be created.
- The default value is _None_.

### `iColor`

- An _Integer_ specifying the contact color.
- The default value is 65280.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {11,12,13,14,15}
Geometry.Part.Cube(iPartColor=12537679)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6250449)

Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_M", 
                        crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_S", 
                        crlTargets=[Face(24)])

created_contact = Connections.Contacts.MSCNastran.ManualGroup(strName="ContactMSCNastran_1", 
                                                              nastranContact=NASTRAN_CONTACT(dRROR=0.0005), 
                                                              crplTarget=[CursorPair(Group(1), 
                                                                                     Group(2))], 
                                                              iColor=16711680)

JPT.Debugger(created_contact)
```
