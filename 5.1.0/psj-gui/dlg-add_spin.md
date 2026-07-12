---
id: dlg-add_spin
title: dlg.add_spin()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Add a Spin to the creating dialog
---

## Description

Add a Spin to the creating dialog.

## Syntax

```psj
dlg.add_spin(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the created component.
- This is a required input.

### `min`

- An _Double_ specifying the minimum value of the Spin range.
  If `type` is _spin.double_, the value will be rounded up.
- This is a required input.

### `max`

- An _Double_ specifying the maximum value of the Spin range.
  If `type` is _spin.double_, the value will be rounded up.
- This is a required input.

### `pos`

- An _Double_ specifying the initial value (starting position) of the Spin range.
  If `type` is _spin.double_, the value will be rounded up.
- This is a required input.

### `increment`

- An _Double_ specifying the increment step of the Spin.
  If `type` is _spin.double_, the value will be rounded up.
- This is a required input.

### `layout`

- A _String_ specifying the created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.
- This is a required input.

### `type`

- An _Enum_ specifying type of Spin:
  - spin.integer: Integer type
  - spin.double: Double type
- The default value is spin.integer.

### `precision`

- An _Integer_ specifying the precision (number of digits after zero) of the input value.
  If `type` is _spin.integer_, this input will be ignored.
- The default value is 1.

## Return Code

This function does not have output value.

## Sample Code

```psj {5-7}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_spin(name="Spin2",min=1,max=100,pos=2,increment=2,layout="Window")
    dlg.add_spin(name="Spin3",type=spin.double,min=0.000000,max=50.000000,pos=1.500000,
        increment=1.500000,precision=3,layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
