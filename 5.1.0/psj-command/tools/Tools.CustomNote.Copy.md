---
id: Tools-CustomNote-Copy
title: Tools.CustomNote.Copy()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Copy custom notes.
---

## Description

Copy custom notes.

## Syntax

```psj
Tools.CustomNote.Copy(...)
```

Macro: CopyCustomNote

Ribbon: <menuselection>Tools &#187; CustomNote &#187; Copy</menuselection>

## Inputs

### `strSrcDocumentName`

- A _String_ specifying name of document that have original custom notes to copy.
- The default value is ''.

### `strDestDocumentName`

- A _String_ specifying name of document that the indicated custom notes will be copied.
- The default value is ''.

### `crlTargets`

- A _List of Cursor_ specifying original custom notes to copy.
- The default value is [].

### `strlNames`

- A _List of String_ specifying names of copied custom notes.
- The default value is [].

### `crCollection`

- A _Cursor_ specifying a collection where original custom notes will be copied.
- The default value is _None_.

### `bKeep`

- A _Boolean_ specifying whether or not 
- The default value is _False_.

## Return Code

A _Boolean_ specifying copy custom note works successfully or not.


## Sample Code

```psj{26-31}
# Create a custom note and collection in document 1.
doc1=JPT.GetActiveDocument()
original_cnote=Tools.CustomNote.Create(
    strNoteName="CustomNote_1", 
    dlNotePosition=[0.0, 0.0, 0.0], 
    strParentName="Collection_1", 
    listContent=["Original Note"], 
    iAlignment=1)

# Prepare a new document.
doc2=JPT.CreateNewDocument()

# Create a custom note and collection in a new document (document 2).
Tools.CustomNote.Create(
    strNoteName="CustomNote_1", 
    dlNotePosition=[0.0, 0.0, 0.0], 
    strParentName="Collection_1", 
    listContent=["Note in new doc"], 
    iAlignment=1)

cnotes_collections=JPT.GetAllByTypeID(JPT.DItemType.CUSTOM_NOTE_COLLECTION)

# Copy custom note in document 1 to document 2.

if cnotes_collections:
    Tools.CustomNote.Copy(
        strSrcDocumentName=doc1.docName, 
        strDestDocumentName=doc2.docName, 
        crlTargets=[original_cnote], 
        strlNames=["CustomNote_1(Copied)"], 
        crCollection=CustomNoteCollection(cnotes_collections[0].id))

JPT.Exec('ViewSpreadNote()')
```
