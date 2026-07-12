---
id: Properties-Section-Delete
title: Properties.Section.Delete()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Delete the create property sections in 1D properties section library
---

## Description

Delete the create property sections in 1D properties section library.

## Syntax

```psj
Properties.Section.Delete(...)
```

Ribbon: <menuselection>Properties &#187; Section &#187; Delete</menuselection>

## Inputs

### `crlSections`

- A _List of Cursor_ specifying the list of property sections will be deleted.
- This is a required input.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {5}
Properties.Section.AddGeneral(strName="abc", 
                              iSecGenType=2, 
                              dDsecGensizeT1=0.02)

creating_status = Properties.Section.Delete(crlSections=[SectionGeneral(1)])

JPT.Debugger(creating_status)
```
