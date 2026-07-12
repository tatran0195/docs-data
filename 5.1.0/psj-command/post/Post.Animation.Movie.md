---
id: Post-Animation-Movie
title: Post.Animation.Movie()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Export animation as a movie file.
---

## Description

Export animation as a movie file.

## Syntax

```psj
Post.Animation.Movie(...)
```

Macro: [CmdPostAnimationExportMovieToFile](../../macro/post/CmdPostAnimationExportMovieToFile)


Ribbon: <menuselection>Post &#187; Animation &#187; Movie</menuselection>

## Inputs

### `strFilePath`

- A _String_ specifying path of movie file including extension indicates file format.
- The default value is ''.

### `strEncoder`

- A _String_ specifying encoder. This option can use if movie type is mpeg4.
- The default value is 'h264'.

### `iFPS`

- An _Integer_ specifying FPS.
- The default value is 8.

### `iRepeat`

- An _Integer_ specifying repeat number.
- The default value is 1.

### `bMakeImage`

- A _Boolean_ specifying whether or not export every frames of the movie to image files.
- The default value is _False_.

### `iWidth`

- An _Integer_ specifying width of export movie.
- The default value is 1920.

### `iHeight`

- An _Integer_ specifying height of export movie.
- The default value is 1080.

### `iBackGroundColor`

- An _Integer_ specifying background color.
  - 0: Use current background color.
  - 1: Set background color to White.
  - 2: Set backgroun color to transparent (only if .gif movie). 
- The default value is 0.

### `bOptimized`

- A _Boolean_ specifying whether or not using Optimization Toolkit.
- The default value is _False_.
  
## Return Code

A _Boolean_ specifying succeeded or failed.

## Sample Code

```psj{25-31}
import os

samplePath = os.path.join(JPT.GetProgramPath(),r"SampleData\PSJ\PSJ-Utility\PostSample\101_solid.op2")
Home.ImportResults.Nastran(strPath=samplePath)

# Show contour
Post.ShowContour(
    crPostJob=TSVPostJob(1), 
    lContourSettings=[
        PostContourSetting(
            postResultKey=PostResultKey(
                iAnalysisType=1, iResultSet=1, iTimeStep=1, strResultName="Displacement", 
                strResultCompName="Translational", iResultPos=1), 
                postDataOp=PostDataOp(iResultLocation=1, iOptionCoord=1))])

Post.ShowDeformation(
    crPostJob=TSVPostJob(1), 
    postResultKey=PostResultKey(
        iAnalysisType=1, iResultSet=1, iTimeStep=1, strResultName="Displacement", strResultCompName="Translational"))
Post.EnableMiddleNodes()

temp_folder=JPT.GetAppPathInfo(JPT.PathType.TEMP_PATH)
outputPath = os.path.join(temp_folder,"101_solid_movie.mp4")

Post.Animation.Movie(
    strFilePath=outputPath, 
    strEncoder="h264", 
    iFPS=8, 
    iRepeat=1, 
    iWidth=882, 
    iHeight=441)
```
