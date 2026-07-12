---
id: dlg-get_item_text
title: dlg.get_item_text()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get text inside the component
---

## Description

Get text inside the component.

## Syntax

```psj
dlg.get_item_text(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the component which user want to get text.
- This is a required input.

## Return Code

A _String_ specifying the text inside the component.

## Sample Code

```psj {3}
from pyjdg import *
def onGetButtonClicked(dlg):
    print(dlg.get_item_text(name="TextBox1"))

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_textbox(name="TextBox1",layout="Window")
    dlg.add_button(name="Button2",text="Get text",width=60,height=22,layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.on_command(name="Button2",callfunc=onGetButtonClicked)

if __name__=='__main__':
    main()
```
