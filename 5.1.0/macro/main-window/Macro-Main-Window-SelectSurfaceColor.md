---
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
id: SelectSurfaceColor
title: SelectSurfaceColor()
---
## Description

Select faces that have the same color as the selected face.

## Syntax

```psj
SelectSurfaceColor(cursor face, bool )
```

## inputs

### `cursor`

- A _Cursor_ that specify the target face.
- This input is required.

### `bool`

- A _Boolean_ value that defines the search scope.
  - _True_: Searches for faces with the same color within the part that contains the face specified in cursor.
  - _False_: Searches for faces with the same color across the entire model.

## Return Code

- A list of _Cursor_ (string format) for the detected faces.
  
## Sample Code

```psj
SelectSurfaceColor(6:21, 0)
```