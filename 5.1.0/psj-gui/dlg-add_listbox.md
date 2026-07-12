---
id: dlg-add_listbox
title: dlg.add_listbox()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Add a ListBox to the creating dialog
---

## Description

Add a ListBox to the creating dialog.

## Syntax

```psj
dlg.add_listbox(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the created component.
- This is a required input.

### `layout`

- A _String_ specifying the created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.
- This is a required input.

### `multisel`

- A _Boolean_ specifying the permission that allow user to select multiple values at the same time:
  - _True_: user can select multiple values.
  - _False_: user can select only one value per time.
- The default value is False.

### `options`

- A _List of String_ specifying all the options of the ListBox component.
- The default value is [].

### `width`

- An _Integer_ specifying the width of the ListBox.
- The default value is 0.

### `height`

- An _Integer_ specifying the height of the ListBox.
- The default value is 0.

## Return Code

This function does not have output value.

## Sample Code

```psj {5-6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_listbox(name="ListBox3",multisel=True,
      options=["item1","item2","item3"],width=100,height=150,layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")

    dlg.generate_window()
if __name__=='__main__':
    main()
```
