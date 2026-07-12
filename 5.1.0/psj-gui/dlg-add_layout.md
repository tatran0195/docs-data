---
id: dlg-add_layout
title: dlg.add_layout()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Add a Layout to the creating dialog
---

## Description

Add a Layout to the creating dialog.

## Syntax

```psj
dlg.add_layout(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the created component.
- This is a required input.

### `layout`

- A _String_ specifying the created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.
- This is a required input.

### `orientation`

- An _Orientation object_ specifying the arrangement direction of inside components:
  - _orientation.horizontal_: all components inside are arranged horizontally.
  - _orientation.vertical_: all components inside are arranged vertically.
- This is a required input.

### `margin`

- A _List_ specifying all the values defining the positions of the creating Layout.
  The list of positions is defined in the order of [left,top,right,bottom].
- The default value is [].

## Return Code

This function does not have output value.

## Sample Code

```psj {5}
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",orientation=orientation.horizontal,margin=[0,10,0,10],layout="Window")
    dlg.add_label(name="Label2",text="Jupiter",layout="Layout1")
    dlg.add_textbox(name="TextBox3",layout="Layout1")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
