---
id: dlg-set_slider_bothtics
title: dlg.set_slider_bothtics()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Show tick marks on both/one side of the SliderBar
---

## Description

Show tick marks on both/one side of the SliderBar.

## Syntax

```psj
dlg.set_slider_bothtics(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the SliderBar.
- This is a required input.

### `enabled`

- A _Boolean_ specifying the way to display tick mark:
  - _True_: show tick mark on both side of the SliderBar.
  - _False_: show tick mark only on one side of the SliderBar.
- This is a required input.

## Return Code

This function does not have output value.

## Sample Code

```psj {7}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add_slider(name="Slider3",width=200,height=100,min=0,max=100,pos=0,layout="Layout1")
    dlg.set_slider_bothtics(name="Slider3",enabled=True)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
