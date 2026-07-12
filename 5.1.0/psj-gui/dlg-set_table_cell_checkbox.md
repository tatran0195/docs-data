---
id: dlg-set_table_cell_checkbox
title: dlg.set_table_cell_checkbox()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Set checkbox cell in the Table
---

## Description

Set checkbox cell in the Table.

## Syntax

```psj
dlg.set_table_cell_checkbox(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the Table component.
- This is a required input.

### `row`

- An _Integer_ specifying the order of row (starts from 0).
- This is a required input.

### `col`

- An _Integer_ specifying the order of column (starts from 0).
- This is a required input.

### `text`

- A _String_ specifying text which will be displayed next to the checkbox.
- This is a required input.

### `checked`

- A _Boolean_ specifying the state of checkbox.
  - _True_: the checkbox is checked.
  - _False_: the checkbox is unchecked.
- The default value is _False_.

## Return Code

This function does not have output value.

## Sample Code

```psj {15-16}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_table(name="Table2",width=260,height=260,
        columns=["Heading1","Heading2"],
        rows=5,layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",
        layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.set_table_cell_checkbox(name="Table2",row=0,
        col=0,text="Checkbox",checked=True)

if __name__=='__main__':
    main()
```
