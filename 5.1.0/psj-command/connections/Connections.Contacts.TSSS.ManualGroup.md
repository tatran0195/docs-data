---
id: Connections-Contacts-TSSS-ManualGroup
title: Connections.Contacts.TSSS.ManualGroup()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Define contact settings between specified groups for TechnoStar SunShine solver
---

## Description

This method defines a contact setting between specified groups for TechnoStar SunShine solver.

## Syntax

```psj
Connections.Contacts.TSSS.ManualGroup(...)
```

Ribbon: <menuselection>Connections &#187; Contacts &#187; SunShine &#187; Manual Group</menuselection>

## Inputs

### `strName`

- A _String_ specifying the contact name.
- The default value is "ContactTS_SS_1".

### `sunshineContact`

- A _[SUNSHINE_CONTACT](./../../data-type/psj-command/parameter-types/SUNSHINE_CONTACT)_ specifying the Sunshine contact parameters.
- The default value is _[SUNSHINE_CONTACT](./../../data-type/psj-command/parameter-types/SUNSHINE_CONTACT)_.

### `crplTarget`

- A _List of Pairs of Cursor_ specifying the pair of master and slave groups.
- The default value is [].

### `crEdit`

- A _Cursor_ specifying an existing SunShine contact setting. If this argument is specified, the specified SunShine contact setting will be modified. If unspecified, a new SunShine contact setting will be created.
- The default value is _None_.

### `iColor`

- An _Integer_ specifying the contact-to-display marker color.
- The default value is 0.

### `iMethod`

- An _Integer_ specifying the method.
- The default value is 1.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj {10-12}
Geometry.Part.Cube()

Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=4803000)

Connections.Contacts.SunShine.ManualFace(crlMasterFaces=[Face(24)], crlSlaveFaces=[Face(49)],
    strName="ContactSunShine_1", sunshineContact=SUNSHINE_CONTACT(dERROR=0.001, dFRIC=0.5,
    dSLIDE=DFLT_DBL, iICOORD=DFLT_INT, dSFACT=DFLT_DBL, dSFACTT=0.5, dCDAMP=DFLT_DBL),
    iContactColor=16711680)

Connections.Contacts.TSSS.ManualGroup(strName="ContactSunShine_2", iColor=16711680,
    sunshineContact=SUNSHINE_CONTACT(dERROR=1e-06, dFRIC=0.5, dSLIDE=DFLT_DBL, iICOORD=DFLT_INT,
    dSFACT=DFLT_DBL, dSFACTT=0.5, dCDAMP=DFLT_DBL), crplTarget=[CursorPair(Group(1), Group(2))])
```
