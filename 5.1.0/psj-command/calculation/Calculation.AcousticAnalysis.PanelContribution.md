---
id: Calculation-AcousticAnalysis-PanelContribution
title: Calculation.AcousticAnalysis.PanelContribution()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create a plot line for each panel property based on Actran's element contribution results
---

## Description

Create a plot line for each panel property based on Actran's element contribution results.

## Syntax

```psj
Calculation.AcousticAnalysis.PanelContribution(...)
```

Macro: [PostToolAcousticPanelContribution](../../macro/calculation/PostToolAcousticPanelContribution)

Ribbon: <menuselection>Calculation &#187; AcousticAnalysis &#187; PanelContribution</menuselection>

## Inputs

### `ilLoadCases`

- A _List of Integer_ specifying the selected loadcases for the element contribution plot line.
- The default value is [].

### `crlProperties`

- A _List of Cursor_ specifying the property panels for the element contribution plot line.
- The default value is [].

### `iAreaUnit`

- An _Integer_ specifying the area unit.
- The default value is 0.

### `bSum`

- A _Boolean_ specifying whether to sum the element contributions.
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying the created panel contribution.

## Sample Code

```psj {8-12}
# Please set path to your sample Nastran Vibro-Acoustic file.
filePath="C:/Temp/Sample.op2"

# Prepare result model
Home.ImportResults.Nastran(strPath=filePath, dFaceAngle=60.16, dEdgeAngle=60.16, bIsVibro=True)

# AcousticAnalysis.PanelContribution
Calculation.AcousticAnalysis.PanelContribution(ilLoadCases=[201], 
                                                crlProperties=[Property2DShell(50000), 
                                                Property3DSolid(20000, 40000)], 
                                                iAreaUnit=0)
Calculation.AcousticAnalysis.PanelContributionCreateGraph(crlLoadCases=[PostActranLoadCase(1, 2, 3, 4)])
```
