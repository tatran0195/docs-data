---
id: Connections-Contacts-ADVC-ContactTable_Advc
title: Connections.Contacts.ADVC.ContactTable_Advc()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create contacts for ADVC solver by using table
---

## Description

Create contacts for ADVC solver by using table.

## Syntax

```psj
Connections.Contacts.ADVC.ContactTable_Advc(...)
```
Macro: [ContactTable_Advc](../../macro/connections/ContactTable_Advc)

Ribbon: <menuselection>Connections &#187; Contacts &#187; ADVC &#187; ContactTable</menuselection>

## Inputs

### `taContactFound_ADVC`

- A list of _[`TCONTACTTABLEDATA_ADVC`](../../data-type/psj-command/parameter-types/TCONTACTTABLEDATA_ADVC)_ specifying ADVC contact sets.
- The default value is [].


### `taContactDeleted_ADVC`
- A list of _Cursor_ of groups to delete ADVC contacts.
- The default value is [].
  
## Return Code

- A _Boolean_ specifying Succeeded or Failed.
  - True: Succeeded.
  - False: Failed.


## Sample Code

```psj{18}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], 
                   strName="Cube_3", 
                   iPartColor=6417130)
Geometry.Part.Cube(dlOrigin=[0.01, 0.01, 0.0], 
                   strName="Cube_4", 
                   iPartColor=6053060)

# Find Contact
contacts_found = Connections.Contacts.ADVC.FindContactPairs(crlParts=[Part(1, 2, 3, 4)])
for contact in contacts_found:
    contact.iContactType = 0 # General

# Create Contact
Connections.Contacts.ADVC.ContactTable_Advc(taContactFound_ADVC = contacts_found)
```
