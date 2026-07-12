---
id: Properties-Section1D
title: Properties.Section1D()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create 1D Property Sketcher Section
---

## Description

Create 1D Property Sketcher Section

## Syntax

```psj
Properties.Section1D(strName="", iSecType=0, iSecGenType=2, dSecGensizeA=0, dSecGensizeB=0, dSecGensizeH=0, dSecGensizeT1=0, dSecGensizeT2=0, dSecGensizeT3=0, bSecTapered=False, dSecGensizeATap=0, dSecGensizeBTap=0, dSecGensizeHTap=0, dSecGensizeT1Tap=0, dSecGensizeT2Tap=0, dSecGensizeT3Tap=0)
```

Macro: [Property1DSection](../../macro/properties/Property1DSection)

Ribbon: <menuselection>Properties &#187; Section1D</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name.
- The default value is "".

### `iSecType`

- An _Integer_ specifying the section type.
- The default value is 0.

### `iSecGenType`

- An _Integer_ specifying the section general type.
- The default value is 2.

### `dSecGensizeA`

- A _Double_ specifying the section general size a.
- The default value is 0.

### `dSecGensizeB`

- A _Double_ specifying the section general size b.
- The default value is 0.

### `dSecGensizeH`

- A _Double_ specifying the section general size h.
- The default value is 0.

### `dSecGensizeT1`

- A _Double_ specifying the section general size t1.
- The default value is 0.

### `dSecGensizeT2`

- A _Double_ specifying the section general size t2.
- The default value is 0.

### `dSecGensizeT3`

- A _Double_ specifying the section general size t3.
- The default value is 0.

### `bSecTapered`

- A _Boolean_ specifying the section tapered.
- The default value is False.

### `dSecGensizeATap`

- A _Double_ specifying the section general size a tapered.
- The default value is 0.

### `dSecGensizeBTap`

- A _Double_ specifying the section general size tapered.
- The default value is 0.

### `dSecGensizeHTap`

- A _Double_ specifying the section general size h tapered.
- The default value is 0.

### `dSecGensizeT1Tap`

- A _Double_ specifying the section general size t1 tapered.
- The default value is 0.

### `dSecGensizeT2Tap`

- A _Double_ specifying the section general size t2 tapered.
- The default value is 0.

### `dSecGensizeT3Tap`

- A _Double_ specifying the section general size t3 tapered.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.Section1D(strName="", iSecType=0, iSecGenType=2, dSecGensizeA=0, dSecGensizeB=0, dSecGensizeH=0, dSecGensizeT1=0, dSecGensizeT2=0, dSecGensizeT3=0, bSecTapered=False, dSecGensizeATap=0, dSecGensizeBTap=0, dSecGensizeHTap=0, dSecGensizeT1Tap=0, dSecGensizeT2Tap=0, dSecGensizeT3Tap=0)
```
