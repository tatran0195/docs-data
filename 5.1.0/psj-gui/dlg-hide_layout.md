---
id: dlg-hide_layout
title: dlg.hide_layout()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Hide the Layout and all of its children components inside
---

## Description

Hide the Layout and all of its children components inside.

## Syntax

```psj
dlg.hide_layout(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the Layout component.
- This is a required input.

## Return Code

This function does not have output value.

## Sample Code

```psj {20}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label2",text="Label",layout="Layout1")
    dlg.add_textbox(name="TextBox3",layout="Layout1")
    dlg.add_layout(name="Layout4",orientation=orientation.horizontal,layout="Window")
    dlg.add_richeditbox(name="RichEditBox8",text="RichEditBox",width=200,height=200,layout="Layout4")
    dlg.add_layout(name="Layout5",orientation=orientation.horizontal,layout="Window")
    dlg.add_textbox(name="TextBox7",layout="Layout5")
    dlg.add_layout(name="Layout6",orientation=orientation.horizontal,layout="Window")
    dlg.add_combobox(name="ComboBox9",layout="Layout6")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.hide_layout(name="Layout5")

if __name__=='__main__':
    main()
```
