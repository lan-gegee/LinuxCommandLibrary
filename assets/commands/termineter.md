# TAGLINE

智能电表安全测试框架

# TLDR

**启动交互式会话**

```termineter```

**以指定的资源文件启动**

```termineter -r [script.rc]```

**以调试日志级别启动**

```termineter -L DEBUG```

# SYNOPSIS

**termineter** [_options_]

# PARAMETERS

**-h**, **--help**
> 显示帮助信息并退出。

**-v**, **--version**
> 显示版本号并退出。

**-L** _LEVEL_, **--log** _LEVEL_
> 设置日志级别（DEBUG、INFO、WARNING、ERROR、CRITICAL）。

**-r** _FILE_, **--rc-file** _FILE_
> 启动时执行资源文件。

# DESCRIPTION

**termineter** 是一个用于智能电表安全测试的 Python 框架。它实现了 C1218 和 C1219 协议，可通过 ANSI type-2 光学探头配合串口连接经光学接口进行通信。

该工具提供类似 Metasploit 的交互式 Shell，带有读取电表数据表、暴力破解凭据和测试电表安全性的模块。命令包括 **connect**、**disconnect**、**use**、**run**、**set** 和 **show**。

# CAVEATS

需要通过光学探头和串口适配器物理接触智能电表。可从 Kali Linux 软件仓库或 pip 获得。

# INSTALL

```nix: nix profile install nixpkgs#termineter```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[msfconsole](/man/msfconsole)(1), [setoolkit](/man/setoolkit)(1)
