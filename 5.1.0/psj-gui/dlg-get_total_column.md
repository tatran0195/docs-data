---
id: dlg-get_total_column
title: dlg.get_total_column()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get the total number of columns of the Table
---

## Description

Get the total number of columns of the Table.

## Syntax

```psj
dlg.get_total_column(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the Table component.
- This is a required input.

## Return Code

An _Integer_ specifying the total number of columns of the Table.

## Sample Code

```psj {14}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_table(name="Table1",rows=14,
        columns=["Heading1","Heading2"],
        layout="Window",width=260,height=260)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    total_cols = dlg.get_total_column(name="Table1")
    JPT.Debugger(total_cols)

if __name__=='__main__':
    main()
```
