---
id: dlg-add_table_sel_option
title: dlg.add_table_sel_option()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Set combobox cell in the Table
---

## Description

Set combobox cell in the Table.

## Syntax

```psj
dlg.add_table_sel_option(...)
```

## Inputs

### `name`

- A _String_ specifying the name of Table.
- This is a required input.

### `row`

- A _Integer_ specifying the position in the horizontal direction of the cell (starts from 0).
- This is a required input.

### `col`

- A _Integer_ specifying the position in the vertical direction of the cell (starts from 0).
- This is a required input.

### `cell`

- A _[TableCellID](../data-type/psj-gui/TableCellID)_ object specifying the location of cell in Table. This argument is only used when _row_ and _col_ are not specified.
  - TableCellID(row,col) defines a cell object
  - TableCellID.row_number returns row number of the cell
  - TableCellID.col_number returns column number of the cell
- This is a required input.

### `index`

- An _Integer_ specifying the default option to be displayed of the ComboBox.
- The starting value is 0 (first option -> index=0).
- This is a required input.

### `options`

- A _List of String_ specifying the options of the ComboBox.
- The default value is [].

## Return Code

This function does not have output value.

## Sample Code

```psj {6-7}
from pyjdg import *
def main():
    dlg=JDGCreator(title="Dialog",include_apply=False)
    dlg.add_table(name="Table2",width=260,height=160,columns=["Heading1","Heading2"],rows=5,layout="Window")
    dlg.generate_window()
    dlg.add_table_cell_option(name="Table2",cell=TableCellID(0,0),options=["0","2"],index=1)
    dlg.add_table_cell_option(name="Table2",row=0,col=1,options=["0","2"],index=1)
if __name__=='__main__':
    main()
```
