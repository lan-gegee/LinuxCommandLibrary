# TAGLINE

以 ASCII 艺术图显示系统信息

# TLDR

**显示系统信息**

```pfetch```

**使用自定义 ASCII 艺术图显示**

```PF_ASCII="[arch]" pfetch```

**只显示指定的信息字段**

```PF_INFO="[ascii title os kernel uptime]" pfetch```

**禁用颜色**

```PF_COLOR=0 pfetch```

**自定义分隔符**

```PF_SEP=": " pfetch```

# SYNOPSIS

**pfetch**

# ENVIRONMENT

**PF_INFO**
> 要显示的字段（以空格分隔）。

**PF_ASCII**
> 要使用的 ASCII 艺术图（发行版名称或 "off"）。

**PF_COLOR**
> 启用颜色（1）或禁用（0）。

**PF_SEP**
> 标签与值之间的分隔符。

**PF_COL1**
> 标签的颜色。

**PF_COL2**
> 信息的颜色。

**PF_COL3**
> 标题的颜色。

# AVAILABLE INFO FIELDS

**ascii**
> 发行版 ASCII 艺术图。

**title**
> 用户名@主机名。

**os**
> 操作系统。

**host**
> 机器型号。

**kernel**
> 内核版本。

**uptime**
> 系统运行时长。

**pkgs**
> 软件包数量。

**memory**
> 内存占用。

**shell**
> 当前 Shell。

**editor**
> 默认编辑器。

**wm**
> 窗口管理器。

**palette**
> 调色板。

# DESCRIPTION

**pfetch** 以 ASCII 艺术图的形式显示系统信息。它是 neofetch 和 screenfetch 的极简、快速替代方案。

该工具是单个 POSIX Shell 脚本，没有任何依赖。可在 Linux、BSD、macOS 以及其他类 Unix 系统上运行。

配置通过环境变量进行。设置 PF_INFO 可以控制显示哪些字段。设置 PF_ASCII 可以改用不同的发行版标志。

输出默认带有颜色，适合截图和桌面美化。在记录日志或极简环境下可以禁用颜色。

检测功能自动覆盖大量发行版、软件包管理器、窗口管理器和桌面环境。

极简的设计追求速度而非功能齐全。与更重的同类工具相比，它可以瞬间启动。

# CAVEATS

功能比 neofetch 少。一些冷门系统可能无法被识别。与其他替代品相比，ASCII 艺术图比较有限。

# HISTORY

**pfetch** 由 **Dylan Araps** 于 **2019 年**前后创建，是一个极简的系统信息工具。neofetch 同样出自这位作者，而 pfetch 则是为偏爱简洁的用户提供的精简替代品。

# INSTALL

```nix: nix profile install nixpkgs#pfetch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[neofetch](/man/neofetch)(1), [screenfetch](/man/screenfetch)(1), [fastfetch](/man/fastfetch)(1), [macchina](/man/macchina)(1)
