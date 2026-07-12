---
id: dlg-add_hlayout
title: dlg.add_hlayout()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Add a horizontal Layout to the creating dialog
---

## Description

Add a horizontal Layout to the creating dialog.

## Syntax

```psj
dlg.add_hlayout(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the created component.
- This is a required input.

### `layout`

- A _String_ specifying the created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.
- This is a required input.

### `margin`

- A _List_ specifying all the values defining the positions of the creating layout.
  The list of positions is defined in the order of [left,top,right,bottom].
- The default value is [].

## Return Code

This function does not have output value.

## Sample Code

```psj {8}
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label2",text="Jupiter",layout="Layout1")
    dlg.add_textbox(name="TextBox3",layout="Layout1")
    dlg.add_hlayout(name="footer",margin=[0,10,0,10],layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
