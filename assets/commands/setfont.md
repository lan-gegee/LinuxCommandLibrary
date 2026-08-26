# TAGLINE

为 Linux TTY 加载控制台屏幕字体

# TLDR

**更改**终端字体

```setfont [font].gz```

通过指定**完整路径**更改字体

```setfont /usr/share/kbd/consolefonts/[font.psf.gz]```

将字体大小**加倍**

```setfont -d```

**重置**为默认字体

```setfont```

在更改前**保存**当前字体

```setfont -o [saved_font] [new_font]```

为**特定控制台**设置字体

```setfont -C /dev/tty2 [font]```

# SYNOPSIS

**setfont** [_OPTIONS_] [_font.new_...] [**-m** _cmap_] [**-u** _umap_] [**-C** _console_]

# PARAMETERS

**-d**, **--double**
> 将字体大小加倍，适用于高密度显示器。

**-h** _N_, **--font-height** _N_
> 覆盖字体高度（对部分字体有用）。

**-N**, **--default8x**=_N_
> 加载宽度为 _N_ 的内置默认字体（8xN）。

**-o** _file_, **--output-font**=_file_
> 在加载新字体前将上一个字体保存到 _file_。

**-O** _file_, **--output-fullfont**=_file_
> 将上一个字体连同其 Unicode 映射表一起保存到 _file_。

**-om** _file_, **--output-consolemap**=_file_
> 将当前控制台映射表保存到 _file_。

**-ou** _file_, **--output-unicodemap**=_file_
> 将当前 Unicode 映射表保存到 _file_。

**-m** _file_, **--consolemap**=_file_
> 从 _file_ 加载控制台映射或 Unicode 控制台映射。

**-u** _file_, **--unicodemap**=_file_
> 加载描述该字体的 Unicode 映射表。

**-C** _device_, **--console**=_device_
> 在指定的控制台设备上设置字体。

**-f**, **--force**
> 即使 Unicode 映射为空也强制加载。

**-R**, **--reset**
> 将控制台字体、大小和 Unicode 映射恢复为启动时的默认值。

**-v**, **--verbose**
> 启用详细输出。

**-V**, **--version**
> 打印版本并退出。

# DESCRIPTION

**setfont** 将控制台屏幕字体加载到 Linux 虚拟终端（TTY）的 EGA/VGA 字符发生器中。它可以加载 PSF（PC Screen Font）文件，并可选择关联 Unicode 映射表以正确显示字符。

字体通常存储在 **/usr/share/kbd/consolefonts/** 中，有多种尺寸（8x8、8x14、8x16）。该命令默认作用于当前控制台，但可以通过 **-C** 指定特定 TTY。不带参数调用时会加载默认的 8x8 字体。

# CAVEATS

仅适用于 Linux 虚拟控制台（TTY），不适用于 xterm 或 GNOME Terminal 等终端模拟器。修改控制台设置需要相应权限（通常为 root）。字体更改重启后不会保留；systemd 系统请在 **/etc/vconsole.conf** 中配置，其他系统使用相应的 init 脚本。

# HISTORY

**setfont** 是 **kbd**（键盘和控制台工具）软件包的一部分，自 **20 世纪 90 年代初**起就是标准的 Linux 组件。PSF 字体格式是专为 Linux 控制台字体开发的。该命令由更早的工具（如 **loadfont**）演化而来，并集成了 Linux **2.0** 时代加入的 Unicode 支持。

# INSTALL

```apt: sudo apt install kbd```

```dnf: sudo dnf install kbd```

```pacman: sudo pacman -S kbd```

```apk: sudo apk add kbd```

```zypper: sudo zypper install kbd```

```nix: nix profile install nixpkgs#kbd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[showconsolefont](/man/showconsolefont)(8), [loadkeys](/man/loadkeys)(1), [consolechars](/man/consolechars)(8)
