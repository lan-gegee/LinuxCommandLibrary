# TAGLINE

Linux 内核管理器与活动监视器

# TLDR

**启动内核模块管理器**

```kmon```

**设置刷新率**（毫秒）

```kmon -t [ms]```

**设置主色调**

```kmon -c [color]```

**以 Unicode 方块标题启动**

```kmon -u```

**以反转的模块列表启动**

```kmon -r```

# SYNOPSIS

**kmon** [_options_]

# PARAMETERS

**-t**, **--tickrate** _MS_
> 设置终端 UI 的刷新率（毫秒）。

**-c**, **--color** _COLOR_
> 设置主色调 [默认：darkgray]。支持：black、red、green、yellow、blue、magenta、cyan、gray、darkgray、lightred、lightgreen、lightyellow、lightblue、lightmagenta、lightcyan、white，或十六进制值。

**-a**, **--accent-color** _COLOR_
> 设置强调色 [默认：white]。

**-r**, **--reverse**
> 反转内核模块列表的顺序。

**-u**, **--unicode**
> 为方块标题显示 Unicode 符号。

**-E**, **--regex**
> 将模块搜索查询解释为正则表达式。

# DESCRIPTION

**kmon** 提供一个基于文本的用户界面，用于管理 Linux 内核模块和监视内核活动。它支持加载、卸载、列入黑名单以及显示内核模块信息，全部通过交互式终端界面完成。

该 TUI 实时显示内核活动，并支持在已加载模块之间导航，查看每个模块的详细信息。

# CAVEATS

加载和卸载内核模块需要 root 权限。仅在 Linux 系统上可用。

# HISTORY

**kmon** 由 **Orhun Parmaksız**（orhun）创建，以 **Rust** 编写。它致力于成为 Linux 内核管理的标准工具，同时支持大多数 Linux 发行版。

# INSTALL

```apt: sudo apt install kmon```

```pacman: sudo pacman -S kmon```

```apk: sudo apk add kmon```

```nix: nix profile install nixpkgs#kmon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lsmod](/man/lsmod)(8), [modprobe](/man/modprobe)(8), [modinfo](/man/modinfo)(8)
