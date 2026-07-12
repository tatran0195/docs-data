---
id: Connections-Contacts-CheckPattern
title: Connections.Contacts.CheckPattern()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Check the mesh pattern on the selected faces. The matched/unmatched mesh pattern between selected entities will be shown based on the selected option
---

## Description

Check the mesh pattern on the selected faces. The matched/unmatched mesh pattern between selected entities will be shown based on the selected option.

## Syntax

```psj
Connections.Contacts.CheckPattern(...)
```

Ribbon: <menuselection>Connections &#187; Contacts &#187; Check Pattern</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the parts to be checked.
- This is a required input.

### `bShowMismatch`

- A _Boolean_ specifying whether to display the part where the mesh pattern does not matches.
- The default value is _False_.

### `bShowMatch`

- A _Boolean_ specifying whether to display the part where the mesh pattern matches.
- The default value is _True_.

### `dTolerance`

- A _Double_ specifying the distance between faces to detect the mesh pattern.
- The default value is 0.01.

## Return Code

Two lists of cursor list: first list contains the entities mesh pattern matched, second list contains the entities mesh pattern isn't match.

## Sample Code

```psj {13}
Geometry.Part.Cube(iPartColor=12276667)

Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                   strName="Cube_2",
                   iPartColor=14511581)

Connections.Contacts.NXNastran.ManualFace(crlFaceMasters=[Face(24)],
                                          crlFaceSlaves=[Face(49)],
                                          dSearchDist=10.0,
                                          dPenaltyFactor=1.0,
                                          iContactColor=16711680)

checking_status = Connections.Contacts.CheckPattern(crlParts=[Part(1, 2)])

JPT.Debugger(checking_status)
```
