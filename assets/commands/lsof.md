# TAGLINE

列出打开的文件

# TLDR

**列出所有打开的文件**

```lsof```

**某用户打开的文件**

```lsof -u [username]```

**某进程打开的文件**

```lsof -p [pid]```

**占用某端口的文件**

```lsof -i :[port]```

**网络连接**

```lsof -i```

**目录中的文件**

```lsof +D [/path/to/dir]```

**使用某文件的进程**

```lsof [/path/to/file]```

**查找已取消链接但仍打开的文件**（磁盘被占满时很有用）

```sudo lsof +L1```

**仅获取 PID**，便于管道传给 kill

```lsof -t -i :[port]```

每 5 秒**监视一个连接**

```lsof -i :[port] -r [5]```

# SYNOPSIS

**lsof** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要检查的特定文件。

**-u** _USER_
> 某用户打开的文件。

**-p** _PID_
> 某进程打开的文件。

**-i** [_ADDR_]
> 网络连接。

**+D** _DIR_
> 目录中的文件。

**-c** _COMMAND_
> 由命令名以 _COMMAND_ 开头的进程打开的文件。

**-n**
> 不将网络编号转换为主机名（更快）。

**-P**
> 不将端口号转换为服务名。

**-t**
> 精简输出：只列出 PID（便于管道传给 **kill**）。

**-F** _FIELDS_
> 供机器解析的字段格式化输出（如 **-Fpcu** 输出 PID、命令、用户）。

**-r** [_seconds_]
> 循环模式：每 _seconds_ 秒（默认 15）重新列出，直到被中断。

**+L1**
> 只显示链接计数小于 1 的文件（即已取消链接但仍然打开——用于找出占满磁盘的"已删除但仍打开"的文件）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lsof**（List Open Files）是一个诊断工具，报告运行中进程当前打开的所有文件。在类 Unix 系统中，"文件"的概念远不止磁盘上的普通文件——它还包括网络套接字、Unix 域套接字、管道、设备文件和目录。每个打开的文件在内部由一个文件描述符表示，lsof 将这些描述符映射回持有它们的进程。

这使得 lsof 成为众多场景下不可或缺的排障工具。它可以识别哪个进程在监听特定的 TCP/UDP 端口（`-i :port`）、找出阻止文件系统卸载的进程（`+D /mount`），或揭示某个程序建立的网络连接。输出包括进程名、PID、用户、文件描述符号、文件类型以及文件路径或网络地址，全面展现进程与系统资源的交互方式。

# CAVEATS

没有 root 权限时，**lsof** 只能看到你自己进程打开的文件。输出可能非常长；可配合 **-c**、**-u** 或 **-i** 进行过滤。**+D** 会递归遍历，在大目录树上可能很慢——非递归列出请改用 **+d**。

# HISTORY

lsof 由 **Vic Abell** 于 1988 年创建，现已成为标准的 Unix 诊断工具。

# INSTALL

```apt: sudo apt install lsof```

```dnf: sudo dnf install lsof```

```pacman: sudo pacman -S lsof```

```apk: sudo apk add lsof```

```zypper: sudo zypper install lsof```

```brew: brew install lsof```

```nix: nix profile install nixpkgs#lsof```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fuser](/man/fuser)(1), [netstat](/man/netstat)(8), [ss](/man/ss)(8), [ps](/man/ps)(1)
