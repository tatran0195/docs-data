---
id: Home-Preferences-Import
title: Home.Preferences.Import()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import settings of Preferences (.json file)
---

## Description

Export settings of Preferences (.json file).

## Syntax

```psj
Home.Preferences.Import(...)
```

Macro: ImportPreferenceSettings

Ribbon: <menuselection>Home &#187; Preferences &#187; Import</menuselection>

## Inputs

### `strPath`

- A _String_ specifying import file path.
- This is a required input.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj
Home.Preferences.Import("C:/temp/DCADPreference.json")
```
