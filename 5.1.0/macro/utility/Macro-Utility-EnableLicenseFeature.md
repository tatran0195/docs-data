---
id: EnableLicenseFeature
title: EnableLicenseFeature()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Turn ON / OFF indicated license.

## Syntax

```psj
EnableLicenseFeature(String License, int Status)
```

## Inputs

### `1. String`

License feature shown in Home \> Preference \> License.

### `2. Int`

- 1: Turn ON the license feature.
- 0: Turn OFF the license feature.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
EnableLicenseFeature("JPT_ANNAS", 0)
```
