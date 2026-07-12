---
id: Tools-GroupByDCS
title: Tools.GroupByDCS()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create node groups according to the nodal coordinate system.
---

## Description

Create node groups according to the nodal coordinate system.

## Syntax

```psj
Tools.GroupByDCS()
```

Ribbon: <menuselection>Tools &#187; GroupByDCS</menuselection>

## Inputs

None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{22}
#Prepare model
Geometry.Part.Cube(
    ilAxialNodes=[4, 4, 4], 
    iPartColor=7463537)
Tools.Coordinates.Face(
    strName="CRect_4", 
    veclPoint=[[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], 
    crItem=Face(24))

#Find target face
faces=JPT.Exec('FindEntities("-10,5,5","Face", 0)')

#Get ids from the result and input into Face function.

ditem_list=JPT.MacroListTCursorToListDItem(faces)
ids=[ditem.id for ditem in ditem_list]

#Create nodal coordinate system for the nodes in the selected face. 
Tools.DisplacementCS(crlInst=[Face(*ids)], crCoordSystem=Coord(1))

#Create node groups according to the nodal coordinate system.
Tools.GroupByDCS()
```
