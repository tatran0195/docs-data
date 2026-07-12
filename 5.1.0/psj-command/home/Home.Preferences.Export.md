---
id: Home-Preferences-Export
title: Home.Preferences.Export()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Export settings of Preferences (.json file)
---

## Description

Export settings of Preferences (.json file).

## Syntax

```psj
Home.Preferences.Export(...)
```

Macro: ExportPreferenceSettings

Ribbon: <menuselection>Home &#187; Preferences &#187; Export</menuselection>

## Inputs

### `strPath`

- A _String_ specifying export file path.
- This is a required input.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj
Home.Preferences.Export("C:/temp/DCADPreference.json")
```
