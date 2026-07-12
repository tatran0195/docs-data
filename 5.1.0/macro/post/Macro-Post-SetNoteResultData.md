---
id: SetNoteResultData
title: SetNoteResultData()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Set the display of result data title in the note window.

## Syntax

```psj
SetNoteResultData(int NoteResultTitle, string NoteResultTitle)
```

## Inputs

### `1. Int`

An Integer specifying the method to display the result data title as default or user-defined name.

### `2. String`

A String specifying an arbitrary user-defined name for result data title.

## Return Code

- "1": Succeeded.
- "0": Failed.

## Sample Code

```psj
SetNoteResultData(1, "Result Data")
```
