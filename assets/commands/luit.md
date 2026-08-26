# TAGLINE

在终端编码与应用程序编码之间进行转换

# TLDR

**以编码转换方式运行命令**

```luit -encoding [ISO-8859-1] [command]```

**以指定编码连接远程主机**

```luit -encoding [EUC-JP] ssh [host]```

**强制使用特定区域设置**

```luit -encoding [GB2312] -x```

**列出支持的编码**

```luit -list```

**以编码转换方式运行 shell**

```luit -encoding [KOI8-R]```

# SYNOPSIS

**luit** [_options_] [_command_]

# PARAMETERS

_COMMAND_
> 要以编码转换方式运行的命令。

**-encoding** _ENC_
> 字符编码。

**-x**
> 在子进程结束时退出。

**-list**
> 列出编码。

**-g** _N_
> GL 字符集。

**--help**
> 显示帮助信息。

# DESCRIPTION

**luit** 在终端编码与应用程序编码之间进行转换。它让 UTF-8 终端能够运行旧式应用程序。

该工具充当终端与应用程序之间的过滤器，翻译字符编码。

# CAVEATS

X11 工具。可能无法处理所有编码。对复杂旧式编码的支持有限。

# HISTORY

luit 为 **XFree86/X.Org** 而创建，用于处理运行 UTF-8 的终端的编码转换。

# INSTALL

```apt: sudo apt install luit```

```dnf: sudo dnf install luit```

```pacman: sudo pacman -S luit```

```zypper: sudo zypper install luit```

```brew: brew install luit```

```nix: nix profile install nixpkgs#luit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xterm](/man/xterm)(1), [iconv](/man/iconv)(1), [locale](/man/locale)(1)
