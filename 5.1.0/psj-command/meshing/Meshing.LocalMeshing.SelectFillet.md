---
id: Meshing-LocalMeshing-SelectFillet
title: Meshing.LocalMeshing.SelectFillet()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Select all the existing fillet faces based on the selected entities
---

## Description

Select all the existing fillet faces based on the selected entities.

## Syntax

```psj
Meshing.LocalMeshing.SelectFillet(...)
```

Ribbon: <menuselection>Meshing &#187; LocalMeshing &#187; SelectFillet</menuselection>

## Inputs

### `crlParts`

- A _List of Cursor_ specifying the list of target parts to search for fillet faces.
- The default value is [].

### `crlFaces`

- A _List of Cursor_ specifying the list of target faces to search for fillet faces.
- The default value is [].

### `dMinArcLength`

- A _Double_ specifying the minimum length of fillet edge in meter. This is a search criterion.
- The default value is 0.0.

### `dMaxArcLength`

- A _Double_ specifying the maximum length of fillet edge in meter. This is a search criterion.
- The default value is 0.009.

### `dMinArcRadius`

- A _Double_ specifying the minimum radius of fillet edge in meter. This is a search criterion.
- The default value is 0.0.

### `dMaxArcRadius`

- A _Double_ specifying the maximum radius of fillet edge in meter. This is a search criterion.
- The default value is 1.0.

### `bConvex`

- A _Boolean_ to enable (_True_) or disable (_False_) the search for convex fillet.
- The default value is _True_.

### `bConcave`

- A _Boolean_ to enable (_True_) or disable (_False_) the search for concave fillet.
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying the found fillet faces if succeeded, or None if failed.

## Sample Code

```psj {4,5}
Geometry.Part.Cube()
Geometry.MakeFillet(crlEdges=[Edge(18, 19, 15)])

faces = Meshing.LocalMeshing.SelectFillet(crlParts=[Part(1)], 
                                          crlFaces=[])
                                        
JPT.Debugger(faces)
```
