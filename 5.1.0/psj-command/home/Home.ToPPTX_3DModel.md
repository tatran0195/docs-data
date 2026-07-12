---
id: Home-ToPPTX_3DModel
title: Home.ToPPTX_3DModel()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Save the model in the current document as a 3D object (.glb file) and embed it into a .pptx file.
---

## Description

Save the model in the current document as a 3D object (.glb file) and embed it into a .pptx file.

## Syntax

```psj
Home.ToPPTX(...)
```

Ribbon: <menuselection>Home &#187; ToImage &#187; 3D Model(*.glb)</menuselection>

## Inputs

This function does not require any input value.
 
## Return Code

A _Boolean_ specifying the status of the process:

- _True_: The model is saved as a 3d model file in pptx.
- _False_: The model is saved as a 3d model file in pptx.

## Sample Code

```psj {5}
Geometry.Part.Cube()
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

Home.ToPPTX_3DModel()
```
