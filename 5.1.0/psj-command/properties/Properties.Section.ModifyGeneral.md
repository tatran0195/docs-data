---
id: Properties-Section-ModifyGeneral
title: Properties.Section.ModifyGeneral()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Modify the existing general section for 1D Property.
---

## Description

Modify the existing general section for 1D Property.

## Syntax

```psj
Properties.Section.ModifyGeneral(...)
```

Macro: Property1DSectionModify_General

Ribbon: <menuselection>Properties &#187; Section &#187; ModifyGeneral</menuselection>

## Inputs

### `strName`

- A _String_ specifying the section name.
- The default value is "".

### `crSection`

- A _Cursor_ specifying the existing section to modify.
- The default value is _None_.

### `iSecType`

- An _Integer_ specifying the section type.
- The default value is 0.

### `iGeneralType`

- An _Integer_ specifying the general type.
- The default value is 0.

### `dA`

- A _Double_ specifying the a.
- The default value is 0.

### `dB`

- A _Double_ specifying the b.
- The default value is 0.

### `dH`

- A _Double_ specifying the h.
- The default value is 0.

### `dT1`

- A _Double_ specifying the t1.
- The default value is 0.

### `dT2`

- A _Double_ specifying the t2.
- The default value is 0.

### `dT3`

- A _Double_ specifying the t3.
- The default value is 0.

### `bTapered`

-A _Boolean_ specifying whether or not tapered.
- The default value is _False_.

### `dDaTap`

- A _Double_ specifying the a tapered.
- The default value is 0.

### `dDbTap`

- A _Double_ specifying the b tapered.
- The default value is 0.

### `dDhTap`

- A _Double_ specifying the h tapered.
- The default value is 0.

### `dDt1Tap`

- A _Double_ specifying the t1 tapered.
- The default value is 0.

### `dDt2Tap`

- A _Double_ specifying the t2 tapered.
- The default value is 0.

### `dDt3Tap`

- A _Double_ specifying the t3 tapered.
- The default value is 0.

### `iDirType`

- An _Integer_ specifying direction type.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {5-9}
Properties.Section.AddGeneral(  strName="t1", 
                                iSecGenType=2, 
                                dDsecGensizeT1=0.001, 
                                iDirType=1)
Properties.Section.ModifyGeneral(strName="t1", 
                                crSection=SectionGeneral(1), 
                                iGeneralType=2, 
                                dT1=0.001, 
                                iDirType=3)
```
