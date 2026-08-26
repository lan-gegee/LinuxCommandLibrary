# TAGLINE

检查库升级之后哪些守护进程需要重启

# TLDR

**列出**过时的进程

```needrestart```

**交互式重启服务**

```sudo needrestart```

以**详细**模式列出

```needrestart -v```

以**静默**模式列出

```needrestart -q```

检查**内核**是否过时

```needrestart -k```

检查 **CPU 微码**是否过时

```needrestart -w```

以**批处理**模式列出（非交互式）

```needrestart -b```

使用指定的**配置文件**

```needrestart -c [path/to/config]```

# SYNOPSIS

**needrestart** [**-v**|**-q**] [**-k**] [**-w**] [**-b**] [**-c** _config_]

# PARAMETERS

**-v**
> 详细模式；显示更多细节

**-q**
> 静默模式；抑制输出

**-k**
> 检查正在运行的内核是否过时

**-w**
> 检查 CPU 微码是否过时

**-b**
> 批处理模式；非交互式，适合脚本

**-l**
> 仅列出；不提示重启

**-r _mode_**
> 重启模式：i（交互式）、a（自动）、l（仅列出）

**-c _config_**
> 使用指定的配置文件

**-p**
> 启用 nagios 插件模式的输出

**-f _frontend_**
> 选择前端：debconf、stdio、readline

# DESCRIPTION

**needrestart** 检查库升级之后哪些守护进程需要重启。共享库更新时，正在运行的进程可能仍在内存中使用旧版本，导致安全漏洞未被修复。

该工具扫描运行中的进程是否使用了已被删除的库文件（说明库已更新），并找出应当重启的服务。它还能检查需要重启系统才能生效的过时内核和 CPU 微码。

# CAVEATS

重启服务可能造成短暂中断。内核和微码更新需要完全重启系统。某些进程可能难以识别或重启。配合 sudo 运行可启用交互式重启提示。

# HISTORY

**needrestart** 由 **Thomas Liske** 为基于 Debian 的系统开发，帮助管理员找出软件包更新后需要重启的服务。它与 apt 集成，可在升级完成后自动运行。

# INSTALL

```dnf: sudo dnf install needrestart```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [apt](/man/apt)(8), [checkrestart](/man/checkrestart)(1)
