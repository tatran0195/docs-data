---
id: dlg-set_combobox_sel
title: dlg.set_combobox_sel()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Set current selection to the ComboBox component
---

## Description

Set current selection to the ComboBox component.

## Syntax

```psj
dlg.set_combobox_sel(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the ComboBox component.
- This is a required input.

### `option`

- An _Integer_ or _String_ specifying the order of the ComboBox component's values or the name of selected item.
- This is a required input.

## Return Code

This function does not have output value.

## Sample Code

```psj {13}
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",margin=[0,0,100,0],orientation=orientation.horizontal,layout="Window")
    dlg.add_combobox(name="ComboBox2",options=["item1","item2","item3","item4","item5"],width=70,layout="Layout1")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.set_combobox_sel(name="ComboBox2",option=3)

if __name__=='__main__':
    main()
```
