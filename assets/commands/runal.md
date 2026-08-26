# TAGLINE

面向终端的创意编程环境

# TLDR

**运行创意编程 sketch**

```runal [sketch.js]```

**将动画导出为 GIF**

```runal --export gif [sketch.js]```

**以自定义画布尺寸运行**

```runal --width [80] --height [40] [sketch.js]```

# SYNOPSIS

**runal** [_options_] _script_

# PARAMETERS

**--export** _FORMAT_
> 将输出导出到文件。支持的格式：png、gif、mp4。

**--width** _COLUMNS_
> 以列数设置画布宽度。

**--height** _ROWS_
> 以行数设置画布高度。

# DESCRIPTION

**runal** 是一个基于文本的创意编程环境，类似于 Processing 或 p5.js，但它把一切都渲染为终端中的文本。它可以用 JavaScript 编程，也可以作为 Go 包使用。它支持 2D 图形、三角函数和颜色，并且可以导出为 PNG、GIF 或 MP4。

# HISTORY

**runal** 由 **Xavier Godart**（emprcl）创建，使用 **Go** 编写。

# INSTALL

```aur: yay -S runal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[figlet](/man/figlet)(1), [terminaltexteffects](/man/terminaltexteffects)(1), [t-rec](/man/t-rec)(1)
