---
id: CmdGeneralReportLinearStatic
title: CmdGeneralReportLinearStatic()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Create report of linear static analysis.

## Syntax

```psj
CmdGeneralReportLinearStatic(string file, bool ExportPPT, bool ExportImgFile)
```

## Inputs

### `1. string `

CSV file path for setting file.

### `2.bool `

Export PPT flag.

### `3.bool `

Export Image File flag.

## Return Code

Nothing.

## Sample Code

```psj
CmdGeneralReportLinearStatic("C:/temp/gen_pre.csv", 1, 0)
```
