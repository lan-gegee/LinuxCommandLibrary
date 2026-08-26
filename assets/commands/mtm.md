# TAGLINE

极简终端复用器

# TLDR

**启动 mtm**

```mtm```

**以特定的 Shell 启动**

```mtm -s [/bin/zsh]```

**以自定义终端类型启动**

```mtm -t [screen-256color]```

# SYNOPSIS

**mtm** [_-s shell_] [_-t term_] [_options_]

# PARAMETERS

**-s** _SHELL_
> 终端中运行的 Shell。

**-t** _TERM_
> 终端类型（TERM 环境）。

**-T** _TERM_
> 要模拟的终端类型。

**-c** _CHAR_
> 命令前缀字符。

# KEY BINDINGS

**Ctrl-G c**
> 创建新终端（水平分割）。

**Ctrl-G C**
> 创建新终端（垂直分割）。

**Ctrl-G n**
> 聚焦下一个终端。

**Ctrl-G p**
> 聚焦上一个终端。

**Ctrl-G h/j/k/l**
> 按方向聚焦终端。

**Ctrl-G w**
> 删除当前终端。

**Ctrl-G Ctrl-G**
> 向终端发送 Ctrl-G。

# DESCRIPTION

**mtm**（Micro Terminal Multiplexer）是一个极简的终端复用器。它将一个终端分割成多个虚拟终端，每个虚拟终端运行自己的 Shell。

该工具采用简单的键盘接口，以 Ctrl-G 作为命令前缀。水平和垂直分割可以构建灵活的布局，焦点可通过方向键在各终端之间移动。

与 tmux 或 screen 不同，mtm 追求极简主义。它没有会话、窗口管理和丰富的配置。这种简洁性使它适合基本的分屏终端需求。

终端模拟支持 UTF-8 和基本的 VT100/VT220 序列。与功能完备的复用器相比，复杂应用可能无法正确渲染。

小巧的代码库让 mtm 易于理解和修改。当 tmux 或 screen 不可用或显得大材小用时，它就派上用场了。

# CAVEATS

功能集极为精简。不支持分离/重连。终端模拟能力有限。没有脚本功能或配置文件。

# HISTORY

**mtm** 由 **Rob King** 编写，是大型终端复用器的极简替代方案。它证明了有用的终端复用只需很少的代码就能实现。

# INSTALL

```apk: sudo apk add mtm```

```brew: brew install mtm```

```nix: nix profile install nixpkgs#mtm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmux](/man/tmux)(1), [screen](/man/screen)(1), [dvtm](/man/dvtm)(1), [abduco](/man/abduco)(1)
