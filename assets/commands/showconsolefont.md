# TAGLINE

显示 Linux 控制台字体的字形

# TLDR

以表格形式**显示当前控制台字体**

```showconsolefont```

**只显示字体信息**而不打印字形表

```showconsolefont --info```

**显示指定控制台设备的字体**

```showconsolefont --console=[/dev/tty1]```

**以详细输出显示**

```showconsolefont --verbose```

# SYNOPSIS

**showconsolefont** [**-C** _console_] [**-v**] [**-V**] [**-h**] [**-i**]

# PARAMETERS

**-i**, **--info**
> 不打印字体表，只显示 ROWSxCOLSxCOUNT 后退出。

**-C**, **--console=**_DEV_
> 指定要使用的控制台设备。参数是一个路径名（如 /dev/tty1）。

**-v**, **--verbose**
> 输出更详细的信息，例如该字体是否为 Unicode 字体。

**-V**, **--version**
> 打印版本号。

**-h**, **--help**
> 打印用法信息。

# DESCRIPTION

**showconsolefont** 将当前 EGA/VGA 控制台屏幕字体输出到标准输出。它以表格形式显示当前已加载字体中的字形（字符），让你可以看到所有可用的字符。

该命令可用于排查 Linux 控制台上的字体渲染问题、在使用 **setfont** 之后验证特定字体是否已加载，或为脚本确定字体特性。使用 **--info** 选项时，它只输出字体尺寸和字符数量，不显示完整的字形表。

# CAVEATS

此命令只能在 Linux 控制台（虚拟终端）上工作，不能用于 X11 或 Wayland 下的终端模拟器。需要访问控制台设备，可能需要相应权限。在使用 framebuffer 控制台的系统上，输出反映的是当前加载的 PSF（PC Screen Font）文件。

# HISTORY

**showconsolefont** 是 **kbd** 项目的一部分，这是一套用于管理 Linux 键盘和控制台字体的工具集。kbd 项目提供的实用工具自 Linux 早期以来一直是控制台配置的重要组成部分。这些工具由更早的控制台工具演化而来，至今仍在维护，供虚拟终端使用。

# INSTALL

```apt: sudo apt install kbd```

```dnf: sudo dnf install kbd```

```pacman: sudo pacman -S kbd```

```apk: sudo apk add kbd```

```zypper: sudo zypper install kbd```

```nix: nix profile install nixpkgs#kbd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[setfont](/man/setfont)(8), [consolechars](/man/consolechars)(8), [loadkeys](/man/loadkeys)(1), [dumpkeys](/man/dumpkeys)(1)
