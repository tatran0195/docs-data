---
id: Post-SetNote-ResultElemNodeID
title: Post.SetNote.ResultElemNodeID()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set the node ID or element ID of the entity to be displayed in the note window
---

## Description

Set the node ID or element ID of the entity to be displayed in the note window.

## Syntax

```psj
Post.SetNote.ResultElemNodeID(...)
```

Macro: [SetNoteResultElemNodeID](../../macro/post/SetNoteResultElemNodeID)

Ribbon: <menuselection>Post &#187; SetNote &#187; ResultElemNodeID</menuselection>

## Inputs

### `bNoteResultElemNodeID`

- A _Boolean_ specifying whether to display the ID of Elements/Nodes in the note window.
- The default value is _True_.

### `iNoteResultElemNodeID`

- An _Integer_ specifying the method to display the Element/Node ID title as default or user-defined name.
    - 0: Default
    - 1: User-Defined
- The default value is 0.

### `strNoteResultElemNodeID`

- A _String_ specifying an arbitrary user-defined name for the Element/Node ID title. This option was used when _iNoteResultElemNodeID_= 1.
- The default value is "".

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {25,27}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Plot the result
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=2, 
                iResultSet=1, 
                iTimeStep=1, 
                strResultName="Stress", 
                strResultCompName="Mises", 
                iResultPos=2), 
                postDataOp=PostDataOp(iResultLocation=2))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Stress", 
                    strResultCompName="Mises"))
Post.Note.Element(crlTargets=[ROElem(448)])

# Hide Element ID information
Post.SetNote.ResultElemNodeID(bNoteResultElemNodeID=False)
# User defines Element ID title
Post.SetNote.ResultElemNodeID(iNoteResultElemNodeID=1, strNoteResultElemNodeID="ELem/NodeID")
```
