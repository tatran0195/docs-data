---
id: dlg-enable_tabwnd_swap_tab
title: dlg.enable_tabwnd_swap_tab()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Set to enable/disable swap the tab items in a tabwnd
---

## Description

Set to enable/disable swap the tab items in a tabwnd.

## Syntax

```psj
dlg.dlg.set_item_visible(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the TabWnd.
- This is a required input.

### `enable`

- A _Boolean_ specifying whether to enable/disable swap the tab items:
  - _True_: Enable to swap.
  - _False_: Disable to swap.
- This is a required input.

## Return Code

This function does not have output value.

## Sample Code

```psj {5}
from pyjdg import *
def main():
    dlg=JDGCreator(title="Dialog",include_apply=False)
    dlg.add_tabwnd(name="TabWnd10",width=200,height=200,layout="Window")
    dlg.enable_tabwnd_swap_tab(name="TabWnd10", enable=False)
    dlg.add_tabwnd_page(name="TabWnd10",page_name="TabItem11",page_text="TabItem1")
    dlg.add_tabwnd_page(name="TabWnd10",page_name="TabItem12",page_text="TabItem2")
    dlg.add_tabwnd_page(name="TabWnd10",page_name="TabItem13",page_text="TabItem3")
    dlg.generate_window()
if __name__=='__main__':
    main()
```
