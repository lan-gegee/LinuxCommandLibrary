# TAGLINE

用于照片修饰和图形设计的开源图像编辑器

# TLDR

**启动 GIMP**

```gimp```

**打开一张图片**

```gimp [image.png]```

**打开多张图片**

```gimp [image1.png] [image2.jpg]```

**以无界面的批处理模式运行**

```gimp -i -b '(gimp-quit 0)'```

**启动时不显示启动画面**

```gimp --no-splash```

# SYNOPSIS

**gimp** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要打开的图像文件。

**-b** _COMMAND_, **--batch** _COMMAND_
> 以非交互方式运行批处理命令。可多次出现。

**--batch-interpreter** _PROC_
> 处理批处理命令的解释过程（默认：Script-Fu）。

**-n**, **--new-instance**
> 启动新实例。

**-i**, **--no-interface**
> 无界面运行（用于批处理模式）。

**--no-splash**
> 不显示启动画面。

**-d**, **--no-data**
> 不加载图案、渐变或画笔。

**-f**, **--no-fonts**
> 不加载字体。

**--verbose**
> 显示详细的启动消息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gimp**（GNU Image Manipulation Program）是一个功能强大的开源图像编辑器。它提供照片修饰、图像合成和图像创作工具，支持众多文件格式。

GIMP 具备图层、蒙版、滤镜、色彩调整和绘图工具等特性。它支持通过 Script-Fu 和 Python 进行脚本化自动化。插件架构使其可以深度定制扩展。

# CONFIGURATION

**~/.config/GIMP/3.0/**（或 **~/.config/GIMP/2.10/**）
> 用户配置目录，按主版本分别存放。

**gimprc**
> 主配置文件，包含首选项和工具设置。

**sessionrc**
> 会话配置，保存窗口位置和对话框状态。

# CAVEATS

作为 GTK 应用需要图形环境。处理大图片可能消耗较多内存。插件兼容性因版本而异。

# HISTORY

GIMP 由 **Spencer Kimball** 和 **Peter Mattis** 于 **1995 年**在加州大学伯克利分校发起。它后来成为 GNU 项目的一员，至今仍是最流行的开源图形应用之一。**GIMP 3.0** 于 **2025 年**发布，带来 GTK3 支持和非破坏性编辑。

# INSTALL

```apt: sudo apt install gimp```

```dnf: sudo dnf install gimp```

```pacman: sudo pacman -S gimp```

```apk: sudo apk add gimp```

```zypper: sudo zypper install gimp```

```nix: nix profile install nixpkgs#gimp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[imagemagick](/man/imagemagick)(1), [inkscape](/man/inkscape)(1), [krita](/man/krita)(1)
