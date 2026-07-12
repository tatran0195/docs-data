---
id: JPT-CSVExportFormatSetting
title: JPT.CSVExportFormatSetting()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Set export format of CSV file as with/without BOM.
---

## Description

Set export format of CSV file as with/without BOM.

## Syntax

```psj
JPT.CSVExportFormatSetting(int Selection)
```

## Inputs

### `int`
- Selection of export format. 0: without BOM, 1: with BOM.
- This is a required input.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {1}
JPT.CSVExportFormatSetting(0)
```
