---
id: Properties-ElemRelatedInfo-Bush
title: Properties.ElemRelatedInfo.Bush()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Modify information such as direction vectors and end releases for the selected bush elements, individually
---

## Description

Modify information such as direction vectors and end releases for the selected bush elements, individually

## Syntax

```psj
Properties.ElemRelatedInfo.Bush(...)
```

Ribbon: <menuselection>Properties &#187; ElemRelatedInfo &#187; Bush</menuselection>

## Inputs

### `listERIBushData`

- A _List of [ERIBUSH_DATA](../../data-type/psj-command/parameter-types/ERIBUSH_DATA) class_ specifying the element related information of bush.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {6-12}
Geometry.Part.Cube(iPartColor=6409934)
Connections.SpringsDampers.Bush.TwoNodes(
    crlMaster=[Node(53)], 
    crlSlave=[Node(61)], 
    iOriMode=1)
ret = Properties.ElemRelatedInfo.Bush(
    listERIBushData=[
        ERIBUSH_DATA(
            iElemId=1089, 
            iEndA=53, 
            iEndB=61, 
            dlOrientVec=[0.0, 1.0, 0.0])])
print(ret)
```
