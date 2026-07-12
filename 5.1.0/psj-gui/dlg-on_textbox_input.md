---
id: dlg-on_textbox_input
title: dlg.on_textbox_input()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Bind a created function to a textbox component when its text is changed
---

## Description

Bind a created function to a textbox component when its text is changed.

## Syntax

```psj
dlg.on_textbox_input(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the TextBox component using for binding a created def function.
- This is a required input.

### `callfunc`

- The name of function wants to be bound to.
- This is a required input.

### `bool`

- A _Boolean_ specifying whether to validate the textbox.
- This is a required input.

## Return Code

This function does not have output value.

## Sample Code

```psj {13}
from pyjdg import *
def on_input(dlg):
    text=dlg.get_item_text("TextBox2")
    if text=="1":
        return False
    else :
        print("Hello")
        return True
def main():
    dlg=JDGCreator(title="Dialog",include_apply=False)
    dlg.add_textbox(name="TextBox2",layout="Window")
    dlg.generate_window()
    dlg.on_textbox_input("TextBox2",on_input,True)
if __name__=='__main__':
    main()
```
