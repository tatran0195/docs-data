---
id: dlg-set_icon_file
title: dlg.set_icon_file()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Set icon for the creating GUI
---

## Description

Set icon for the creating GUI dialog.

## Syntax

```psj
dlg.set_icon_file(...)
```

## Inputs

### `file`

- A _String_ specifying the full path of the icon file using to set the icon for the creating GUI dialog.
- This is a required input.

## Return Code

This function does not have output value.

## Sample Code

```psj {8}
from pyjdg import *

def main():
    sel_ico = JPT.GetProgramPath() + \
        r"Lib\site-packages\win32\test\win32rcparser\python.ico"

    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.set_icon_file(file=sel_ico)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
