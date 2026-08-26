# TAGLINE

通过点击识别屏幕像素的颜色

# TLDR

**选取颜色**：点击一个像素并打印其十六进制值

```grabc```

以 **RGB 分量**形式将所选颜色**打印**到标准错误

```grabc -rgb```

**打印**鼠标点击处的**窗口 id** 而不是颜色

```grabc -W```

使用窗口 id 和坐标**读取**已知像素的颜色，**无需点击**

```grabc -w [window_id] -l +[x]+[y]```

**打印全部 16 位**颜色深度而不是默认的高 8 位

```grabc -a```

# SYNOPSIS

**grabc** [_options_]

# DESCRIPTION

**grabc** 是一个小巧的 X Window 工具，用于报告屏幕像素的颜色。不带参数运行时，鼠标指针会变成十字准星；点击任意像素后，该像素的颜色会以十六进制字符串（带 **#** 前缀）的形式打印到标准输出，而对应的 RGB 分量值则写入标准错误。

由于十六进制值输出到 stdout、RGB 值输出到 stderr，脚本中可以分别捕获两者，例如把十六进制字符串赋给 shell 变量，同时让 RGB 分解值直接打印到终端。这使得 grabc 非常适合从任何运行中的应用、壁纸或图像中取样颜色，以便在配置文件、主题或绘图程序中复用。

给定窗口 id 和像素坐标时，grabc 还能以非交互方式读取颜色，这对自动化和测试很有用。

# PARAMETERS

**-v**
> 显示版本信息。

**-h**
> 显示用法帮助。

**-hex**
> 将像素值以十六进制打印到标准输出（默认行为）。

**-rgb**
> 将像素值以 RGB 分量打印到标准错误。

**-W**
> 打印鼠标点击位置所在窗口的 id。

**-w**  _id_
> 十六进制窗口 id；与 **-l** 配合可非交互地读取像素。

**-l**  _+x+y_
> 要取样的像素坐标；需要配合 **-w** 提供窗口 id。

**-d**
> 显示调试消息。

**-a**
> 打印全部 16 位颜色；默认只报告高 8 位。

# CAVEATS

grabc 需要正在运行的 X11 服务器并链接 Xlib，因此在没有 XWayland 等 X 兼容层的纯 Wayland 会话中无法工作。报告的值反映屏幕上实际绘制的内容，包括合成器效果、色彩配置文件或透明度混合的影响，可能与源图像的标称颜色不同。

# HISTORY

grabc 由 **Muhammad A Muquit** 编写，首次发布于 **1997 年 3 月 16 日**。它至今仍是一个用途单一、体积小巧的工具，以 C 源码形式分发，针对 libX11 构建。

# INSTALL

```apt: sudo apt install grabc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xprop](/man/xprop)(1), [xwininfo](/man/xwininfo)(1), [import](/man/import)(1), [convert](/man/convert)(1)

# RESOURCES

```[Source code](https://github.com/muquit/grabc)```

```[Homepage](https://www.muquit.com/muquit/software/grabc/grabc.html)```

<!-- verified: 2026-06-22 -->
