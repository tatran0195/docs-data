---
id: FileMenu-LoadPOH5
title: FileMenu.LoadPOH5()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Open .poh5 / .poh5a file.
---

## Description

Open .poh5 / .poh5a file.

## Syntax

```psj
FileMenu.LoadPOH5(...)
```

Ribbon: <menuselection>FileMenu &#187; LoadPOH5</menuselection>

## Inputs

### `strFileName`

- A _String_ specifying the file name.
- This is a required input.

### `iSaveOption`

- An _Integer_ specifying the save option. 
- It always set 0 for this function.
  
## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{3}
# Prepare a poh5 / poh5a file to read
poh5_filepath = "C:/temp/mydata.poh5"

FileMenu.LoadPOH5(poh5_filepath)
```
