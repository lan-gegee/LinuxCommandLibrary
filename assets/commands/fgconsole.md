# TAGLINE

打印前台虚拟终端编号

# TLDR

打印**当前**终端编号

```fgconsole```

打印**下一个**未分配的虚拟终端编号

```fgconsole --next-available```

# SYNOPSIS

**fgconsole** [_options_]

# DESCRIPTION

**fgconsole** 打印前台虚拟终端的编号。如果终端是串行终端，则打印 "serial" 而不是编号。

它是 kbd 软件包中控制台管理实用工具的一员。

# PARAMETERS

**-n**, **--next-available**
> 打印下一个未分配的 VT 编号

**-V**, **--version**
> 打印版本号并退出

**-h**, **--help**
> 显示帮助并退出

# CAVEATS

只能在 Linux 控制台上工作。不在虚拟终端上时返回错误。属于 kbd 软件包。

# INSTALL

```apt: sudo apt install kbd```

```dnf: sudo dnf install kbd```

```pacman: sudo pacman -S kbd```

```apk: sudo apk add kbd```

```zypper: sudo zypper install kbd```

```nix: nix profile install nixpkgs#kbd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chvt](/man/chvt)(1), [deallocvt](/man/deallocvt)(1), [dumpkeys](/man/dumpkeys)(1)
