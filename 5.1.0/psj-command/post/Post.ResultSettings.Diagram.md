---
id: Post-ResultSettings-Diagram
title: Post.ResultSettings.Diagram()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Set up the result settings for displaying the diagram
---

## Description

Set up the result settings for displaying the diagram.

## Syntax

```psj
Post.ResultSettings.Diagram(...)
```

Macro: [CmdPostDiagramSettings](../../macro/post/CmdPostDiagramSettings)

Ribbon: <menuselection>Post &#187; ResultSettings &#187; Diagram</menuselection>

## Inputs

### `postDataVizOptDiagram`

- A _[POST_DATA_VIZ_OPT_DIAGRAM](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_DIAGRAM)_ specifying all settings of the diagram display.
- The default value is [POST_DATA_VIZ_OPT_DIAGRAM](../../data-type/psj-command/parameter-types/POST_DATA_VIZ_OPT_DIAGRAM).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
    - _True_: The process is executed successfully.
    - _False_: Cannot execute the function.

## Sample Code

```psj {1}
Post.ResultSettings.Diagram(postDataVizOptDiagram=PostDataVizOptDiagram(dRatioModel=0.05, dRatioScreen=0.05))
```
