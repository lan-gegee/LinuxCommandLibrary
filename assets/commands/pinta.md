# TAGLINE

简单的图像编辑程序

# TLDR

**打开 Pinta**

```pinta```

**打开图像**

```pinta [image.png]```

**打开多张图像**

```pinta [image1.png] [image2.jpg]```

# SYNOPSIS

**pinta** [_options_] [_files_]

# PARAMETERS

**-h**, **--help**
> 显示帮助。

**-V**, **--version**
> 显示版本。

**--display** _DISPLAY_
> 要打开的 X11 display。

**--gapplication-service**
> 作为后台 D-Bus 服务运行，供其他应用打开文件时调用。

# DESCRIPTION

**pinta** 是一个简单的图像编辑程序。它的灵感来自 Paint.NET，为 Linux 提供了一个易用的编辑器。

核心工具包括选区、画笔、铅笔、形状和文字。图层支持非破坏性编辑。

特效包括模糊、锐化和颜色调整。插件架构支持扩展。

撤销历史支持无限层级。可以随时回退修改。

支持常见格式：PNG、JPEG、BMP、GIF 等。原生格式可保留图层。

# FEATURES

- 图层支持
- 无限撤销
- 绘图工具
- 选区工具
- 特效与调整
- 插件支持

# CAVEATS

不如 GIMP 强大。不支持 CMYK。缺少某些高级功能。

# HISTORY

**Pinta** 始于 **2010 年**，是对 Paint.NET 理念的 C#/GTK 移植。它致力于成为 Linux 上基础图像编辑的 GIMP 简易替代品。

# INSTALL

```apk: sudo apk add pinta```

```zypper: sudo zypper install pinta```

```nix: nix profile install nixpkgs#pinta```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gimp](/man/gimp)(1), [krita](/man/krita)(1), [inkscape](/man/inkscape)(1), [imagemagick](/man/imagemagick)(1)
