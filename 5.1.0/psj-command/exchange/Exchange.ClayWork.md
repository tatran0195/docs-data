---
id: Exchange-ClayWork
title: Exchange.ClayWork()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Make a simple design change for solid mesh parts
---

## Description

Make a simple design change for solid mesh parts.

## Syntax

```psj
Exchange.ClayWork(...)
```

Macro: 

Ribbon: <menuselection>Exchange &#187; ClayWork</menuselection>

## Inputs

### `iProcess`

- An _Integer_ specifying the process type.
	- 0: Sphere
	- 1: Boolean +
	- 2: Boonlean -
- The default value is 0.

### `iWrappingType`

- An _Integer_ specifying the wrapping type. This argument only was used when `iProcess` = 1 or 2.
	- 0: Tight
	- 1: Convex
- The default value is 0.

### `dlSphereCenter`

- A _List of Double_ specifying the center coordinates of sphere.
- The default value is [].

### `dSphereRadius`

- A _Double_ specifying the radius of sphere.
- The default value is 0.0.

### `crTargetPart`

- A _Cursor_ specifying the part to which the wrapped sphere will be added or scraped off. This argument only was used when `iProcess` = 1 or 2.
- The default value is _None_.

## Return Code

A _Boolean_ specifying the function successfully executed or not.

## Sample Code

```psj {15-21,25}
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
Meshing.SolidMeshing(
	crlParts=[Part(1)], 
	dGradingFactor=1.05, 
	dStretchLimit=0.1, 
	iSpeedVsQual=1, 
	iRegion=1, 
	bSafeMode=False, 
	iParallel=16, 
	bInternalMeshOnly=False, 
	iPartColor=65280)

# Add spheres
ret1 = Exchange.ClayWork(
		iProcesstype=0, 
		dlSphereCenter=[
			[0.006, 0.01, 0.002], [0.006, 0.01, 0.003], [0.006, 0.01, 0.004], [0.006, 0.01, 0.006], 
			[0.006, 0.01, 0.007], [0.004, 0.01, 0.007], [0.004, 0.01, 0.006], [0.004, 0.01, 0.004], 
			[0.004, 0.01, 0.003], [0.004, 0.01, 0.002]], 
		dSphereRadius=0.002)
print(ret1)

# Pile up the wrapped sphere
ret2 = Exchange.ClayWork(iProcesstype=1, iWrappingType=1, iFactor = 0.6, crTargetPart=Part(1))
print(ret2)
```
