# TAGLINE

从图像生成配色方案

# TLDR

**从图像生成颜色**

```wal -i [image.png]```

**浅色主题**

```wal -i [image.png] -l```

**跳过设置壁纸**

```wal -i [image.png] -n```

**使用主题**

```wal --theme [theme-name]```

**列出主题**

```wal --theme```

**恢复颜色**

```wal -R```

# SYNOPSIS

**wal** [_-a alpha_] [_-b background_] [_-i image_] [_-l_] [_-n_] [_--theme name_] [_options_]

# PARAMETERS

**-i** _IMAGE_
> 输入图像或图像目录。

**-l**
> 生成浅色配色方案。

**-n**
> 跳过设置壁纸。

**--theme** _NAME_
> 使用主题文件（不带参数使用时可列出主题）。

**-R**
> 恢复上一个配色方案。

**-c**
> 删除所有缓存的配色方案。

**-a** _ALPHA_
> 设置终端背景透明度（仅限 URxvt）。

**-b** _COLOR_
> 要使用的自定义背景色。

**--backend** _BACKEND_
> 要使用的取色后端（不带参数使用时可列出后端）。

**--saturate** _0.0-1.0_
> 设置颜色饱和度级别。

**-o** _SCRIPT_
> wal 完成后要运行的外部脚本。

**-q**
> 静默模式，不输出信息。

**-s**
> 跳过更改终端中的颜色。

**-t**
> 跳过更改 TTY 中的颜色。

# DESCRIPTION

**wal**（pywal）通过从壁纸图像中提取主色调来生成配色方案，并将其应用到终端模拟器、shell 和其他应用程序。它基于单一来源图像，在整个桌面环境中创建统一的视觉主题。

提取出的调色板会实时应用到终端颜色上，并可通过模板系统为其他程序生成配置文件。这让 i3、polybar、rofi 等众多应用自动采用相同的配色方案。

生成的主题会被缓存以便快速切换，之前的配色方案可在登录时恢复。同时支持浅色和深色两种变体，如果只需要颜色，可以跳过设置壁纸的步骤。

# CAVEATS

需要 Python。终端支持程度不一。X11/Wayland 行为有差异。

# HISTORY

**pywal** 的设计目标是从图像生成配色方案并应用到终端和应用程序。

# INSTALL

```apk: sudo apk add py3-pywal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[feh](/man/feh)(1), [wpgtk](/man/wpgtk)(1), [flavours](/man/flavours)(1)
