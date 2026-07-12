---
id: CmdPostAnimationExportMovieToFile
title: CmdPostAnimationExportMovieToFile()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Export animation

## Syntax


```psj
CmdPostAnimationExportMovieToFile(string pathName, string encoder, int fps, int repeat, bool makeImage, int width, int height, int bgcolor)
```

## Inputs

### `1. string `

The full path to the exporting animation.

### `2. string `

Encoder. This option can use if movie type is mpeg4.

### `3. int `

Frame Per Second.

### `4. int `

Repeat.

### `5. bool `

Make Image option. 0: No, 1: Yes.

### `6. int `

Screen width.

### `7. int `

Screen height.

### `9. int `

Background color. 0: Use current background color, 1: Set background color to White, 2: Set backgroun color to transparent (only if .gif movie). 

## Return Code

True: succeeded, False: failed.

## Sample Code

```psj
CmdPostAnimationExportMovieToFile("C:/Temp/animation.gif", "h264", 8, 1, 0, 1378, 708, 0)
```
