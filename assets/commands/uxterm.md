# TAGLINE

启动带 Unicode UTF-8 支持的 xterm

# TLDR

**启动 Unicode 终端**

```uxterm```

**以指定几何尺寸启动**

```uxterm -geometry [80x24]```

**使用指定字体（ISO 10646-1 编码）启动**

```uxterm -fn [fixed]```

**以自定义标题启动**

```uxterm -T "[My Terminal]"```

**启动并运行命令**

```uxterm -e [bash]```

# SYNOPSIS

**uxterm** [_xterm-options_]

# PARAMETERS

所有 xterm 选项都会被透传。常用选项包括：

**-geometry** _WxH+X+Y_
> 设置窗口大小和位置。

**-fn** _font_
> 设置终端字体。

**-fb** _font_
> 设置粗体字体。

**-fg** _color_
> 设置前景色。

**-bg** _color_
> 设置背景色。

**-T** _title_
> 设置窗口标题。

**-e** _command_
> 在终端中运行命令。

**-hold**
> 命令退出后保持窗口打开。

# DESCRIPTION

**uxterm** 是一个包装脚本，用于启动启用了 Unicode（UTF-8）支持的 xterm。它会设置 UXTerm 资源类并启用 UTF-8 模式，适合显示国际字符和符号。

该包装脚本使用系统 locale 来确定字符编码。如果没有设置 locale，则默认为 en_US。locale 工具会在启动前验证系统是否支持所选 locale。

所有命令行参数都会直接传递给 xterm。不应指定 **-class** 和 **-u8** 选项，因为它们由包装脚本设置。字体配置使用 ISO 10646-1 编码的字体。

# CAVEATS

需要支持 UTF-8 的 locale。需要安装合适的 Unicode 字体（Debian 上为 xfonts-base）。如果当前 locale 不支持 UTF-8 字符编码，可能会产生意外的结果。仅限 X11。

# HISTORY

**uxterm** 作为 xterm 的一部分而创建，目的是简化以正确的 Unicode 支持运行终端的过程。随着 Unicode 成为标准，用户需要在不必手动配置 xterm 复杂选项的情况下可靠地显示 UTF-8，它因此应运而生。

# INSTALL

```apt: sudo apt install xterm```

```dnf: sudo dnf install xterm```

```pacman: sudo pacman -S xterm```

```apk: sudo apk add xterm```

```zypper: sudo zypper install xterm```

```brew: brew install xterm```

```nix: nix profile install nixpkgs#xterm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xterm](/man/xterm)(1), [locale](/man/locale)(1)
