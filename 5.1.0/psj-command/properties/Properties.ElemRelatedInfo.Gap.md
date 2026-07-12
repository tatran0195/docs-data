---
id: Properties-ElemRelatedInfo-Gap
title: Properties.ElemRelatedInfo.Gap()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Modify information such as direction vectors and end releases for the selected gap elements, individually
---

## Description

Modify information such as direction vectors and end releases for the selected gap elements, individually.

## Syntax

```psj
Properties.ElemRelatedInfo.Gap(...)
```

Ribbon: <menuselection>Properties &#187; ElemRelatedInfo &#187; Gap</menuselection>

## Inputs

### `listERIGapData`

- A _List of [ERIGAP_DATA](../../data-type/psj-command/parameter-types/ERIGAP_DATA) class_ specifying the element related information of gap.
- The default value is [].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {8-14}
Geometry.Part.Cube(iPartColor=6409934)
Connections.Gaps.TwoNodes(
    crlMaster=[Node(6)], 
    crlSlave=[Node(8)], 
    iOriMode=1, 
    strName="GAP_1", 
    dlOriVec=[0.0, 0.0, 0.0])
ret = Properties.ElemRelatedInfo.Gap(
        listERIGapData=[
            ERIGAP_DATA(
                iElemId=1090, 
                iEndA=6, 
                iEndB=8, 
                dlOrientVec=[0.0, 1.0, 0.0])])
print(ret)
```
