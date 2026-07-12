---
id: Properties-Section-AddGeneral
title: Properties.Section.AddGeneral()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Unknown Description
---

## Description

The general properties of a one-dimensional section are generated.

## Syntax

```psj
Properties.Section.AddGeneral(...)
```

Ribbon: <menuselection>Properties &#187; Section &#187; AddGeneral</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name.
- The default value is "".

### `iSecType`

- An _Integer_ specifying the section type.
- The default value is 0.

### `iSecGenType`

- An _Integer_ specifying the section general type.
- The default value is 0.

### `dDsecGensizeA`

- A _Double_ specifying the section general size a.
- The default value is 0.

### `dDsecGensizeB`

- A _Double_ specifying the section general size b.
- The default value is 0.

### `dDsecGensizeH`

- A _Double_ specifying the section general size h.
- The default value is 0.

### `dDsecGensizeT1`

- A _Double_ specifying the section general size t1.
- The default value is 0.

### `dDsecGensizeT2`

- A _Double_ specifying the section general size t2.
- The default value is 0.

### `dDsecGensizeT3`

- A _Double_ specifying the section general size t3.
- The default value is 0.

### `bBsecTapered`

- A _Boolean_ specifying the bsec tapered.
- The default value is False.

### `dDsecGensizeATap`

- A _Double_ specifying the section general size a tapered.
- The default value is 0.

### `dDsecGensizeBTap`

- A _Double_ specifying the section general size b tapered.
- The default value is 0.

### `dDsecGensizeHTap`

- A _Double_ specifying the section general size h tapered.
- The default value is 0.

### `dDsecGensizeT1Tap`

- A _Double_ specifying the section general size t1 tapered.
- The default value is 0.

### `dDsecGensizeT2Tap`

- A _Double_ specifying the section general size t2 tapered.
- The default value is 0.

### `dDsecGensizeT3Tap`

- A _Double_ specifying the section general size t3 tapered.
- The default value is 0.

### `iDirType`

- An _Integer_ specifying the y direction type.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.Section.AddGeneral(strName="t1", 
                            iSecGenType=2, 
                            dDsecGensizeT1=0.001, 
                            iDirType=1)
```
