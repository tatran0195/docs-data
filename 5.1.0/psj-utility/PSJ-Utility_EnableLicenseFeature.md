---
id: JPT-EnableLicenseFeature
title: JPT.EnableLicenseFeature()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Enable or disable an inputted license feature
---

## Description

Enable/Disable a license feature which is existing in the current Jupiter.

## Syntax

```psj
JPT.EnableLicenseFeature("licenseFeatureName", BoolType)
```

## Inputs

### `licenseFeatureName`

- A _String_ specifying the name of Jupiter license which is existing in the current Jupiter.
- The Jupiter license's name can be found at <menuselection>Home &#187; Preference &#187; License</menuselection>.
- This is a required input.

### `BoolType`

- An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the enable state of license:
  - _True_: Enable the license.
  - _False_: Disable the license.
- This is a required input.

:::tip
You also can input **1** instead of inputting JPT.BoolType.TRUE_VAL,
or input **0** instead of inputting JPT.BoolType.FALSE_VAL.
:::

## Return Code

This utility function does not have output value.

## Sample Code

```psj {2,3,5,8,9,11}
# Disable license JPT_BASE
JPT.EnableLicenseFeature("JPT_BASE",
                         JPT.BoolType.FALSE_VAL)
# Or
# JPT.EnableLicenseFeature("JPT_BASE", 0)

# Enable license JPT_BASE
JPT.EnableLicenseFeature("JPT_BASE",
                         JPT.BoolType.TRUE_VAL)
# Or
# JPT.EnableLicenseFeature("JPT_BASE", 1)
```
