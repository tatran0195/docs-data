---
id: Home-ImportCAD-Parasolid
title: Home.ImportCAD.Parasolid()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Import a parasolid file (*.x_t) to the Jupiter Database
---

## Description

Import a parasolid file (\*.x_t) to the Jupiter Database.

## Syntax

```psj
Home.ImportCAD.Parasolid(...)
```

Ribbon: <menuselection>Home &#187; Import CAD &#187; Parasolid</menuselection>

## Inputs

### `strlPaths`

- A _List of String_ specifying a list of the parasolid files (\*.x_t files) which will be used for importing.
- This is a required input.

### `dChordHeightTolerance`

- A _Double_ specifying the maximum distance from the actual surface to the facet face. The smaller the Chord Height, the smaller the facets the more accurate the curvature of the surface is represented.
- The default value is 0.0.

### `dAngleToleranceDegree`

- A _Double_ specifying the angle tolerance which influences the tessellation of curves with relatively small radii in comparison to the overall size of the CAD model.
- The default value is 7.0.

### `dSurfacePlaneTolerance`

- A _Double_ specifying the maximum divergence distance when converting the original surface into a facet face.
- The default value is 0.0.

### `dSurfacePlaneAngle`

- A _Double_ specifying the maintained areas with the setting angles larger than the angle between facets face of the geometry.
- The default value is 20.0.

### `dMaxFacetWidth`

- A _Double_ specifying the maximum size of a single facet edge.
- The default value is 0.1.

### `dMinFacetWidth`

- A _Double_ specifying the minimum size of a single facet edge.
- The default value is 0.0.

### `dScale`

- A _Double_ specifying the unit ratio imported from the file's unit into the document's unit.
- The default value is 0.001.

### `bUseColorInformation`

- A _Boolean_ specifying whether to read color information in the CAD file.
- The default value is _False_.

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The parasolid file (\*.x_t file) is imported successfully.
- False: The parasolid file (\*.x_t file) cannot be imported.

## Sample Code

```psj {1,2,3,4}
imported_status = Home.ImportCAD.Parasolid(strlPaths=[JPT.GetProgramPath() +
                                                      "SampleData/CAD_Model/Parasolid/BWM_GRABCAD.x_t"],
                                           dAngleToleranceDegree=7.0,
                                           dScale=0.001)
JPT.Debugger(imported_status)
```
