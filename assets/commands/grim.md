# TAGLINE

Wayland 原生截图工具

# TLDR

对**所有输出进行截图**

```grim```

对**特定输出**截图

```grim -o [output_name]```

对**特定区域**截图

```grim -g "[x],[y] [width]x[height]"```

**选择**一个区域并对其截图（配合 slurp）

```grim -g "$(slurp)"```

使用**自定义文件名**

```grim "[path/to/file.png]"```

截图并**复制到剪贴板**

```grim - | wl-copy```

# SYNOPSIS

**grim** [_options_] [_output_]

# PARAMETERS

**-g** _GEOMETRY_
> 捕获特定区域（x,y widthxheight 格式）

**-o** _OUTPUT_
> 捕获特定的 Wayland 输出（显示器）

**-s** _FACTOR_
> 设置缩放系数

**-t** _TYPE_
> 输出格式：png、jpeg 或 ppm

**-q** _QUALITY_
> JPEG 质量（1-100）

**-l** _LEVEL_
> PNG 压缩级别（0-9）

**-c**
> 在截图中包含光标

# DESCRIPTION

**grim**（grab image）是一款 Wayland 原生截图工具。它直接从 Wayland 合成器捕获图像，因此与 Sway、Wayland 上的 GNOME 及其他基于 Wayland 的环境兼容。

对于区域选择，grim 通常与 **slurp** 搭配使用，后者支持交互式选择屏幕区域。输出到标准输出（**-**）可以通过管道传给 **wl-copy** 等剪贴板管理器。

# CAVEATS

仅限 Wayland；在 X11 上无法工作（请改用 scrot 或 maim）。需要支持 screencopy 协议的兼容 Wayland 合成器。某些合成器可能需要额外配置才能启用截图。

# HISTORY

grim 由 Simon Ser（emersion）创建，是 Sway 窗口管理器 Wayland 生态工具的一部分。它提供类似 scrot 等 X11 工具的功能，但专为 Wayland 的安全模型而设计。

# INSTALL

```apt: sudo apt install grim```

```dnf: sudo dnf install grim```

```pacman: sudo pacman -S grim```

```apk: sudo apk add grim```

```zypper: sudo zypper install grim```

```nix: nix profile install nixpkgs#grim```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[slurp](/man/slurp)(1), [wl-copy](/man/wl-copy)(1), [scrot](/man/scrot)(1), [maim](/man/maim)(1)

# RESOURCES

```[Source code](https://git.sr.ht/~emersion/grim)```

<!-- verified: 2026-07-17 -->
