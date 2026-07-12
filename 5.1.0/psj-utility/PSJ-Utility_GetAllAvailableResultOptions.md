---
id: JPT-GetAllAvailableResultOptions
title: JPT.GetAllAvailableResultOptions()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get all available result options of the inputted result type
---

## Description

Get all available result options of the inputted result type.

## Syntax

```psj
JPT.GetAllAvailableResultOptions(PostAnalysisType,
                                 resultSet,
                                 timeStep,
                                 resultName,
                                 componentName,
                                 PostResultDataLoc)
```

## Inputs

### `PostAnalysisType`

- An _Enum_ specifying the _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.
- This is a required input.

### `resultSet`

- An _Integer_ specifying the step ID of the imported result.
- This is a required input.

### `timeStep`

- An _Integer_ specifying the time step of the imported result.
- This is a required input.

### `resultName`

- A _String_ specifying the type of result (Such as Displacement, Stress, etc.).
- This is a required input.

### `componentName`

- A _String_ specifying a specific direction of the result (Such as X, Y, Z, etc.).
- This is a required input.

### `PostResultDataLoc`

- An _Enum_ specifying the _[PostResultDataLoc](../data-type/psj-utility/post-utility/enumeration-types/post-result-data-loc-types)_ describing the location of result (Such as on node, on element, etc.).
- This is a required input.

## Return Code

A _List of [PostDataOp](../data-type/psj-utility/post-utility/post-built-in-types/post-data-op)_ objects specifying all available settings of the working result.

## Sample Code

```psj {5-13}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

all_available_result_options_vector = \
    JPT.GetAllAvailableResultOptions(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                                     1,
                                     1,
                                     "Stress",
                                     "XX",
                                     JPT.PostResultDataLoc.POST_LOC_ON_ELEMENT_NODE
                                    )

JPT.Debugger(all_available_result_options_vector)

for available_PostDataOp in all_available_result_options_vector:
    #Component of AvailablePostDataOp
    print("---------------------------------")
    print("Location: " + str(available_PostDataOp.loc))
    print("Conversion: " + str(available_PostDataOp.cnv))
    print("Continuously: " + str(available_PostDataOp.cont))
    print("Coordinate: " + str(available_PostDataOp.coord))
    print("Load 1D: " + str(available_PostDataOp.load1d))
    print("Load 2D: " + str(available_PostDataOp.load2d))
    print("Complex: " + str(available_PostDataOp.complex))
    print("Phase Angle: " + str(available_PostDataOp.phaseAngle))
    print("User Coordinate ID: " + str(available_PostDataOp.userCoordSysId))
```

<!-- [//]: # "amt is not used in the current version"

<!-- print("Amplitude: " + str(available_PostDataOp.amt)) -->
