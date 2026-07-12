---
id: dlg-add_pagesctrl
title: dlg.add_pagesctrl()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Add a PagesCtrl (wizard type) to the creating dialog
---

## Description

Add a PagesCtrl (wizard type) to the creating dialog.

## Syntax

```psj
dlg.add_pagesctrl(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the created component.
- This is a required input.

### `layout`

- A _String_ specifying the created layout name.
  The created layout can be a GroupBox component, Layout component, etc.
- This is a required input.

### `show_header`

- A _Boolean_ specifying the state of the PageItem's header:
  - _True_: PageItem's header will be shown.
  - _False_: PageItem's header will be hidden.
- The default value is _True_.

### `current_page`

- An _Integer_ specifying the PageItem shown by default (starts from 0).
- The default value is 0.

### `sel_color`

- An _Integer_ specifying the highlight color when selecting a PageItem.
- The default value is 13158460.

### `show_separator`

- A _Boolean_ specifying the stage of separator:
  - _True_: Show the separate border.
  - _False_: Do not show the separate border.
- The default value is _True_.

### `width`

- An _Integer_ specifying the width of the PagesCtrl.
- The default value is 0.

### `height`

- An _Integer_ specifying the height of the PagesCtrl.
- The default value is 0.

### `text_align`

- A _String_ specifying the text alignment type (left-center-right) set for PageItem.
- The default value is "center".

## Return Code

This function does not have output value.

## Sample Code

```psj {5}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_pagesctrl(name="PagesCtrl4",current_page=2,width=300,height=300,text_align="right",layout="Window")
    dlg.add_pageitem(name="PagesCtrl4",page_name="PageItem5",page_header="PageItem 1")
    dlg.add_pageitem(name="PagesCtrl4",page_name="PageItem6",page_header="PageItem 2")
    dlg.add_pageitem(name="PagesCtrl4",page_name="PageItem7",page_header="PageItem 3")
    dlg.add_pageitem(name="PagesCtrl4",page_name="PageItem8",page_header="PageItem 4")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
