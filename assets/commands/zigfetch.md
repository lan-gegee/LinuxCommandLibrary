# TAGLINE

用 Zig 编写的极简 neofetch 风格系统信息工具

# TLDR

**显示系统信息**

```zigfetch```

**显示时不带 ASCII 艺术标志**

```zigfetch --no-logo```

# SYNOPSIS

**zigfetch** [_options_]

# PARAMETERS

**--no-logo**
> 禁用 ASCII 艺术标志显示。

# DESCRIPTION

**zigfetch** 是一款受 neofetch 和 fastfetch 启发的轻量级系统信息显示工具。它在 ASCII 艺术标志旁显示操作系统、内核、运行时间、Shell、CPU、内存等硬件信息。可通过 **~/.config/zigfetch** 下的 config.json 文件进行配置。

# HISTORY

**zigfetch** 由 **utox39** 创建，使用 **Zig** 编写。

# INSTALL

```nix: nix profile install nixpkgs#zigfetch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[neofetch](/man/neofetch)(1), [fastfetch](/man/fastfetch)(1), [screenfetch](/man/screenfetch)(1)
