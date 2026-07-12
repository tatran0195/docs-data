---
id: dlg-add_vertex_selector
title: dlg.add_vertex_selector()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Add "Vertex" to the selection list, allowing user to select vertexes and store the selected vertexes to the selection list
---

## Description

Add "Vertex" to the selection list, allowing user to select vertexes and store the selected vertexes to the selection list.

## Syntax

```psj
dlg.add_vertex_selector(...)
```

## Inputs

### `text`

- A _String_ specifying the title of selector.
- The default value is "".

## Return Code

This function does not have output value.

## Sample Code

```psj {10}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_vertex_selector()
    dlg.generate_window()

if __name__=='__main__':
    main()
```
