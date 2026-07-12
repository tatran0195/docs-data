---
id: dlg-on_groupbox_checked
title: dlg.on_groupbox_checked()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Bind a created def function to a GroupBox's CheckBox
---

## Description

Bind a created def function to a GroupBox's CheckBox.

## Syntax

```psj
dlg.on_groupbox_checked(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the GroupBox using for binding a created def function.
- This is a required input.

### `callfunc`

- The name of function wants to be bound to.
- This is a required input.

## Return Code

This function does not have output value.

## Sample Code

```psj {14}
from pyjdg import *
def on_group_checked(dlg,checked):
    if checked :
        print("checked")
    else:
        print("unchecked")
    print("get checked status==", str(dlg.is_groupbox_checked("GroupBox2")))

def main():
    dlg=JDGCreator(title="Dialog",include_apply=False)
    dlg.add_groupbox(name="GroupBox2",text="GroupBox",layout="Window")
    dlg.set_groupbox_checked(name="GroupBox2",checked=False)
    dlg.add_button(name="Button3",text="Button",width=60,height=22,bk_color=15790320,layout="GroupBox2")
    dlg.generate_window()
    dlg.on_groupbox_checked("GroupBox2",on_group_checked)
if __name__=='__main__':
    main()```
