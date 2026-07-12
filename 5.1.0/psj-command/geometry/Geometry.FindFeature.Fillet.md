---
id: Geometry-FindFeature-Fillet
title: Geometry.FindFeature.Fillet()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Find feature in part by typical description
---

## Description

Find feature in part by typical description

## Syntax

```psj
Geometry.FindFeature.Fillet(crlParts=[], crlFaces=[], dMinAngle=1.0, dMaxAngle=10.0, dMinFaceWidth=1.0, dMaxFaceWidth=10.0, dMinCurveRadius=0.0, dMaxCurveRadius=171, dScale=1.0)
```

Ribbon: <menuselection>Geometry &#187; FindFeature &#187; Fillet</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the part.
- The default value is [].

### `crlFaces`

- A _List of Cursor_ specifying the face.
- The default value is [].

### `dMinAngle`

- A _Double_ specifying the minimum angle.
- The default value is 1.0.

### `dMaxAngle`

- A _Double_ specifying the maximum angle.
- The default value is 10.0.

### `dMinFaceWidth`

- A _Double_ specifying the minimum face width.
- The default value is 1.0.

### `dMaxFaceWidth`

- A _Double_ specifying the maximum face width.
- The default value is 10.0.

### `dMinCurveRadius`

- A _Double_ specifying the minimum curve radius.
- The default value is 0.0.

### `dMaxCurveRadius`

- A _Double_ specifying the maximum curve radius.
- The default value is 171.

### `dScale`

- A _Double_ specifying the scale.
- The default value is 1.0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.FindFeature.Fillet(crlParts=[], crlFaces=[], dMinAngle=1.0, dMaxAngle=10.0, dMinFaceWidth=1.0, dMaxFaceWidth=10.0, dMinCurveRadius=0.0, dMaxCurveRadius=171, dScale=1.0)
```
