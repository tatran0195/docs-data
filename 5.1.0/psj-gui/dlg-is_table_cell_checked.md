---
id: dlg-is_table_cell_checked
title: dlg.is_table_cell_checked()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Check the state of checkbox cell
---

## Description

Check the state of checkbox cell.

## Syntax

```psj
dlg.is_table_cell_checked(...)
```

## Inputs

### `name`

- A _String_ specifying the name of Table.
- This is a required input.

### `cell`

- A _[TableCellID](../data-type/psj-gui/TableCellID)_ object specifying the location of cell in Table.
  - TableCellID(row,col) defines a cell object
  - TableCellID.row_number returns row number of the cell
  - TableCellID.col_number returns column number of the cell
- This is a required input.

## Return Code

A _Boolean_ specifying the state of checkbox cell:

- _True_: The checkbox cell is checked.
- _False_: The checkbox cell is unchecked.

## Sample Code

```psj {10-12}
from pyjdg import *

def on_cell_button_clicked(dlg,name,cell):
    JPT.ClearLog()
    cellvector=dlg.get_table_sel_cell(name="Table2")
    if cellvector.size() > 0:
       check_cell_checkbox = \
            dlg.is_table_cell_checkbox(name="Table2",
                cell=cellvector[0])
       check_state_checkbox = \
            dlg.is_table_cell_checked(name="Table2",
                cell=cellvector[0])
       print("Is checkbox cell: " + str(check_cell_checkbox))
       print("State of checkbox cell: " + \
           str(check_state_checkbox))

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
    dlg.on_table_sel_changed(name="Table2",
        callfunc=on_cell_button_clicked)

if __name__=='__main__':
    main()
```
