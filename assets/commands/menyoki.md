# TAGLINE

命令行截图、录屏与图像操作工具

# TLDR

**截取**焦点窗口的屏幕截图并保存为 PNG

```menyoki capture png save```

将窗口**录制为 GIF 动图**

```menyoki record gif save```

将 GIF **拆分**为单帧图像

```menyoki split [animation.gif]```

通过转换为灰度图来**编辑图像**

```menyoki edit --grayscale [path/to/image] png save```

**分析图像**并打印其详细信息

```menyoki analyze [path/to/image]```

在终端中**查看图像**

```menyoki view [path/to/image]```

# SYNOPSIS

**menyoki** [_flags_] [_options_] _subcommand_

# PARAMETERS

**-v**, **--verbose**
> 提高日志详细程度。

**-q**, **--quiet**
> 不显示输出。

**-c**, **--config** _FILE_
> 设置配置文件。

**--color** _HEX_
> 设置主颜色（默认：3AA431）。

**capture**
> 截取屏幕截图。接受格式子命令（png、jpg、webp、bmp、ico、tiff、tga、pnm、ff、exr）。

**record**
> 录制动画。接受格式子命令（gif、apng）。

**split**
> 将动画拆分为单帧。

**make**
> 用多帧图像合成动画。

**edit**
> 编辑图像。支持 --grayscale、--invert、--convert、--crop、--resize、--rotate、--flip、--blur、--hue、--contrast、--brightness。

**analyze**
> 分析图像并打印其属性。

**view**
> 在终端中查看图像。

# DESCRIPTION

**menyoki** 是一个截图和录屏工具，还能执行各种图像操作，例如制作/拆分 GIF 以及修改/分析/查看图像文件。它最初用于录制终端窗口，也可以适配其他用途。

子命令包括：用于截图的 **capture**、用于录屏的 **record**、用于 GIF 操作的 **split** 和 **make**、用于图像处理的 **edit**、用于图像分析的 **analyze**，以及用于终端显示图像的 **view**。输出格式包括 PNG、JPG、WebP、BMP、ICO、TIFF、PNM 和 GIF/APNG。

操作以子命令链的方式组合：动作子命令是必需的，格式和 **save** 子命令则是可选的。在截图或录制过程中，可通过按键绑定选择目标区域或窗口。

# CAVEATS

Linux 上的屏幕捕获需要 X11。按键绑定仅在截图或录制操作期间生效。

# HISTORY

**menyoki** 由 **Orhun Parmaksız** 创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S menyoki```

```nix: nix profile install nixpkgs#menyoki```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scrot](/man/scrot)(1), [import](/man/import)(1), [ffmpeg](/man/ffmpeg)(1)
