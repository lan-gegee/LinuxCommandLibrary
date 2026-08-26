# TAGLINE

专业数字绘画应用

# TLDR

**打开 Krita**

```krita```

**打开文件**

```krita [image.kra]```

**打开多个文件**

```krita [file1.png] [file2.kra]```

**从命令行导出**

```krita --export --export-filename [output.png] [input.kra]```

**启动时不显示启动画面**

```krita --nosplash```

# SYNOPSIS

**krita** [_options_] [_files_...]

# PARAMETERS

_FILES_
> 要打开的图像文件。

**--export**
> 导出模式。

**--export-filename** _FILE_
> 导出的输出文件。

**--nosplash**
> 禁用启动画面。

**--new-image** _SPEC_
> 创建新图像。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Krita** 是一款专业数字绘画应用。它支持画笔、图层、滤镜和动画。

该工具面向概念艺术家、插画师和纹理艺术家。它具有丰富的画笔自定义功能。

# CAVEATS

资源占用高。画笔包较大。基于 KDE。

# HISTORY

Krita 始于 1999 年 **KOffice** 的组成部分，后来发展为领先的开源数字绘画应用。

# INSTALL

```apt: sudo apt install krita```

```dnf: sudo dnf install krita```

```pacman: sudo pacman -S krita```

```apk: sudo apk add krita```

```zypper: sudo zypper install krita```

```nix: nix profile install nixpkgs#krita```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gimp](/man/gimp)(1), [inkscape](/man/inkscape)(1), [blender](/man/blender)(1)
