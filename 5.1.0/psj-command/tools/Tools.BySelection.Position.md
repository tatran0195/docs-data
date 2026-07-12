---
id: Tools-BySelection-Position
title: Tools.BySelection.Position()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Renumber by position
---

## Description

Renumber by position

## Syntax

```psj
Tools.BySelection.Position(crlTargets=[], iType=0, iMethod=0, iStartID=1, iIncrementStep=1, bAscending1=True, bAscending2=False, bAscending3=False, iSortFirst=0, iSortSecond=1, iSortThird=2, iEnableSortFirst=1, iEnableSortSecond=0, iEnableSortThird=0, iOffset1=0, iOffset2=0, iOffset3=0, dTol1=0.0, dTol2=0.0, dTol3=0.0, crCoord=None, bSpecialFace=False)
```

Macro: RenumberSpecify_byPosition

Ribbon: <menuselection>Tools &#187; BySelection &#187; Position</menuselection>

## Inputs

### `crlTargets`

- A _List of Cursor_ specifying the target.
- The default value is [].

### `iType`

- An _Integer_ specifying the type.
- The default value is 0.

### `iMethod`

- An _Integer_ specifying the method.
- The default value is 0.

### `iStartID`

- An _Integer_ specifying the start ID.
- The default value is 1.

### `iIncrementStep`

- An _Integer_ specifying the increment step.
- The default value is 1.

### `bAscending1`

- A _Boolean_ specifying the ascending1.
- The default value is True.

### `bAscending2`

- A _Boolean_ specifying the ascending2.
- The default value is False.

### `bAscending3`

- A _Boolean_ specifying the ascending3.
- The default value is False.

### `iSortFirst`

- An _Integer_ specifying the sort first.
- The default value is 0.

### `iSortSecond`

- An _Integer_ specifying the sort second.
- The default value is 1.

### `iSortThird`

- An _Integer_ specifying the sort third.
- The default value is 2.

### `iEnableSortFirst`

- An _Integer_ specifying the enable sort first.
- The default value is 1.

### `iEnableSortSecond`

- An _Integer_ specifying the enable sort second.
- The default value is 0.

### `iEnableSortThird`

- An _Integer_ specifying the enable sort third.
- The default value is 0.

### `iOffset1`

- An _Integer_ specifying the offset1.
- The default value is 0.

### `iOffset2`

- An _Integer_ specifying the offset2.
- The default value is 0.

### `iOffset3`

- An _Integer_ specifying the offset3.
- The default value is 0.

### `dTol1`

- A _Double_ specifying the tol1.
- The default value is 0.0.

### `dTol2`

- A _Double_ specifying the tol2.
- The default value is 0.0.

### `dTol3`

- A _Double_ specifying the tol3.
- The default value is 0.0.

### `crCoord`

- A _Cursor_ specifying the coordinate.
- The default value is None.

### `bSpecialFace`

- A _Boolean_ specifying the special face.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{14-26}
# model and environment settings
JPT.Exec('ViewShowID(1)')
Geometry.Part.Cube(ilAxialNodes=[4, 4, 4], iPartColor=7434735)
JPT.ViewFitToModel()

# show current node ids
curl_nodes=MainWindow.RightClick.AssociatedPick(crlInput=[Part(1)], strTarget="Node")
ditem_nodes=JPT.MacroListTCursorToListDItem(curl_nodes)

JPT.SelectionByIDs(JPT.DItemType.NODE, [ditem.id for ditem in ditem_nodes], True)
JPT.MessageBoxPSJ("Check current node IDs", JPT.MsgBoxType.MB_INFORMATION_OK)

# renumber nodes
Tools.BySelection.Position(
    crlTargets=[Node(*[ditem_node.id for ditem_node in ditem_nodes])],
    iMethod=2, 
    bAscending2=True, 
    bAscending3=True, 
    iEnableSortSecond=1, 
    iEnableSortThird=1, 
    iOffset1=100, 
    iOffset2=1000, 
    iOffset3=1, 
    dTol1=1e-05, 
    dTol2=1e-05, 
    dTol3=1e-05)
    
# show renumbered node ids
curl_nodes=MainWindow.RightClick.AssociatedPick(crlInput=[Part(1)], strTarget="Node")
ditem_nodes=JPT.MacroListTCursorToListDItem(curl_nodes)
JPT.SelectionByIDs(JPT.DItemType.NODE, [ditem.id for ditem in ditem_nodes], True)
JPT.MessageBoxPSJ("Node IDs have changed and aligned.", JPT.MsgBoxType.MB_INFORMATION_OK)

```
