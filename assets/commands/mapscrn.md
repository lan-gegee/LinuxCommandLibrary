# TAGLINE

加载输出字符转换映射表

# TLDR

**加载屏幕映射表**

```mapscrn [mapfile]```

**从标准映射目录加载**（解析到 /usr/{share,lib}/kbd/consoletrans 下）

```mapscrn [trivial]```

**加载新表之前将当前映射表保存**到文件

```mapscrn -o [old-map.bin] [new-map]```

**重置为 trivial（恒等）映射**

```mapscrn trivial```

**在指定控制台上应用映射**

```mapscrn -C /dev/tty3 [mapfile]```

# SYNOPSIS

**mapscrn** [_options_] _mapfile_

# PARAMETERS

_MAPFILE_
> 要加载的屏幕映射表。可以是绝对路径，也可以是在 kbd consoletrans 目录（如 **/usr/share/kbd/consoletrans/**）下解析的名称。文件可以是 256 字节二进制、512 字节（Unicode）二进制或文本映射格式。

**-o** _FILE_, **--output**=_FILE_
> 加载新表之前，将先前的映射表保存到 _FILE_。

**-C** _DEV_, **--console**=_DEV_
> 将更改应用到指定的控制台设备（默认：当前 TTY）。

**-v**, **--verbose**
> 详细输出。

**-V**, **--version**
> 打印版本后退出。

**-h**, **--help**
> 打印用法后退出。

# DESCRIPTION

**mapscrn** 为 Linux 文本控制台加载屏幕输出字符映射表。该表告诉内核如何把写入 **/dev/tty**_n_ 的字节转换为当前已加载控制台字体中的字形索引。它与 **loadkeys**（输入映射）和 **setfont**（字形）一起，共同控制传统的 8 位控制台处理管线。

要恢复恒等映射，请加载 **trivial** 表（例如 **mapscrn trivial**）；没有专门的"清除"标志。

# CAVEATS

**mapscrn** 的功能现已内置于 **setfont** 中——现代 kbd 安装保留 **mapscrn** 仅为向后兼容。该命令只对 Linux 文本虚拟终端有效（不适用于终端模拟器或 **fbterm** 等 framebuffer 终端）。在 UTF-8 控制台上很少需要它；应改为加载 Unicode 映射（通过 **setfont** 的 **-u**）。需要足够的权限才能写入控制台。

# HISTORY

**mapscrn** 属于 **kbd** 软件包，这是由 Alexey Gladkov 等人维护的标准 Linux 控制台键盘和字符工具集。

# INSTALL

```apt: sudo apt install kbd```

```dnf: sudo dnf install kbd```

```pacman: sudo pacman -S kbd```

```apk: sudo apk add kbd```

```zypper: sudo zypper install kbd```

```nix: nix profile install nixpkgs#kbd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[setfont](/man/setfont)(8), [loadkeys](/man/loadkeys)(1), [showconsolefont](/man/showconsolefont)(8)
