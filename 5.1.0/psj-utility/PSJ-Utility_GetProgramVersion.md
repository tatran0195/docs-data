---
id: JPT-GetProgramVersion
title: JPT.GetProgramVersion()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get all the version information of the current Jupiter application
---

## Description

Get all the version information of the current Jupiter application.

## Syntax

```psj
JPT.GetProgramVersion()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[VersionInfo](../data-type/psj-utility/pre-utility/built-in-types/VersionInfo)_ object specifying a _List_ containing the version, revision information of the current Jupiter application, including:

- Major
- Minor
- Sub
- Build.

## Sample Code

```psj {2}
# Get the version information of the current Jupiter
version = JPT.GetProgramVersion()
print(f"Jupiter {version.major}.{version.minor}.{version.sub}")
print(f"Revision {version.build}")
```
