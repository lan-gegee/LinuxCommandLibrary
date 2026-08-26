# TAGLINE

用 Rust 编写的系统信息获取工具

# TLDR

**显示系统信息**

```macchina```

**使用指定主题**

```macchina --theme [Hydrogen]```

**只显示指定读数项**

```macchina --show [host,kernel,uptime]```

**以百分比显示内存和磁盘使用情况**

```macchina -m -p```

**显示完整且不截断的内核与运行时长字符串**

```macchina --long-kernel --long-uptime```

**列出可用主题**

```macchina --list-themes```

**诊断配置问题**

```macchina --doctor```

# SYNOPSIS

**macchina** [_--theme name_] [_--show fields_] [_options_]

# PARAMETERS

**-t**, **--theme** _NAME_
> 使用指定名称的主题。

**-o**, **--show** _FIELDS_
> 只显示列出的读数项（逗号分隔）。

**-c**, **--config** _FILE_
> 使用其他配置文件。

**-l**, **--list-themes**
> 列出可用主题并退出。

**-d**, **--doctor**
> 检查配置是否存在问题。

**-m**, **--memory-percentage**
> 以百分比显示内存使用情况。

**-p**, **--disk-space-percentage**
> 以百分比显示磁盘空间使用情况。

**-D**, **--disks**
> 为每个检测到的磁盘显示一行。

**-C**, **--physical-cores**
> 统计物理 CPU 核心数而非逻辑核心数。

**-U**, **--long-uptime**
> 以较长的易读格式呈现运行时长。

**-K**, **--long-kernel**
> 完整呈现内核版本字符串，不截断。

**-S**, **--long-shell**
> 打印用户 Shell 的绝对路径，而不只是其名称。

**-s**, **--current-shell**
> 报告当前进程使用的 shell，而非登录 shell。

**-i**, **--interface** _NAME_
> 报告指定网络接口的地址。

**--ascii-artists**
> 展示内置 ASCII 艺术的作者名单。

**-v**, **--version**
> 显示版本。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**macchina** 是用 Rust 编写的系统信息获取工具。它以可自定义的 ASCII 艺术和主题展示系统细节，类似于 neofetch，但更注重性能。

信息包括：主机名、内核、操作系统、运行时长、软件包、shell、终端、CPU、GPU、内存、磁盘使用情况、电池等。每个字段称为一个"readout"（读数项），可单独显示或隐藏。

主题控制颜色、格式和布局。内置主题从极简到华丽不等。也可以用 TOML 格式创建自定义主题。

ASCII 艺术可以显示发行版标志或自定义图案。图案会适配主题定义的终端颜色，并通过当前激活的主题进行配置，而不是通过专门的命令行选项。

配置保存在 ~/.config/macchina/macchina.toml 中，定义默认主题、可见的读数项、自定义颜色以及 ASCII 设置。

性能是其关键特性——与同类工具相比，macchina 启动迅速且资源占用极少。

# CAVEATS

部分读数项需要特定的系统访问权限。GPU 检测并非在所有系统上都能工作。自定义主题需要正确的 TOML 语法。终端的颜色支持各不相同。某些功能仅限特定平台。

# HISTORY

**macchina** 由 **Uttarayan Mondal**（grtcdr）于 **2020 年**前后创建。为了性能而用 Rust 编写，旨在提供比 neofetch 更快的选择，同时保持可定制性。名字来源于意大利语中的"机器"一词。

# INSTALL

```pacman: sudo pacman -S macchina```

```brew: brew install macchina```

```nix: nix profile install nixpkgs#macchina```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[neofetch](/man/neofetch)(1), [fastfetch](/man/fastfetch)(1), [pfetch](/man/pfetch)(1), [onefetch](/man/onefetch)(1)
