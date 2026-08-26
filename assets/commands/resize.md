# TAGLINE

设置终端环境以匹配窗口大小

# TLDR

让终端报告/更新其**大小**（用于串行控制台）

```resize```

以可供 **shell** 使用的形式打印行数/列数

```resize -s```

# SYNOPSIS

**resize** [**-u** | **-c**] [**-s** [_rows_ _cols_]]

# PARAMETERS

**-s** [_rows_ _cols_]
> 设置终端大小（未给出尺寸时为查询）

**-u**
> 输出适用于 TERMCAP 的 Stretch shell 命令

**-c**
> 输出适用于 TERMCAP 的 C shell 命令

**-v**
> 详细输出；打印所用的转义序列

# DESCRIPTION

**resize** 打印用于将 COLUMNS 和 LINES 环境变量设置为终端当前尺寸的 shell 命令。它与终端模拟器通信以确定实际窗口大小，然后输出可通过求值来更新环境的命令。

当终端窗口被调整大小而程序需要知道新尺寸时，或在串行连接上工作时（此时终端大小可能无法自动检测），该命令特别有用。

# CAVEATS

终端必须支持 VT100 风格的大小查询。输出必须由 shell 求值（例如 **eval \`resize\`**）才能实际设置变量。现代终端模拟器通常通过 SIGWINCH 信号自动更新 COLUMNS 和 LINES。

# HISTORY

属于 **xterm** 工具集，最初为 X Window System 终端模拟器编写。在现代系统上由于终端大小调整通常自动处理而较少需要，但对远程会话和串行控制台仍然有用。

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

[stty](/man/stty)(1), [tput](/man/tput)(1), [xterm](/man/xterm)(1)
