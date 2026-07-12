---
id: MeshEditMoveNodeDeform
title: MeshEditMoveNodeDeform()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Move nodes deform

## Syntax

```psj
MeshEditMoveNodeDeform(int m_solverType,String m_strFilePath,int m_iStep,double m_dScale)
```

## Inputs

### `1. Int`

type of solver

### `2. String`

file path

### `3. Int`

Step

### `4. Double`

value of scale

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeshEditMoveNodeDeform(1,"Test",1,0.001)
```
