# TAGLINE

POSIX 系统配置变量查询工具

# TLDR

列出**所有**可用的配置值

```getconf -a```

列出**特定目录**的配置值

```getconf -a [path/to/directory]```

检查系统是 **32 位还是 64 位**

```getconf LONG_BIT```

检查当前用户同时可运行的**进程数**

```getconf CHILD_MAX```

列出所有配置值并用 **grep** 过滤

```getconf -a | grep MAX```

# SYNOPSIS

**getconf** [_-v spec_] _system_var_
**getconf** [_-v spec_] _path_var_ _pathname_

# PARAMETERS

**-a**
> 显示所有配置变量及其值

**-v** _SPEC_
> 使用规范 _SPEC_ 来确定配置值

**LONG_BIT**
> long 整数的位数（32 或 64）

**CHILD_MAX**
> 每个用户的最大进程数

**OPEN_MAX**
> 进程可同时打开的最大文件数

**PAGE_SIZE**
> 系统内存页大小（字节）

**PATH_MAX**
> 文件路径的最大长度

**HOST_NAME_MAX**
> 主机名的最大长度

**ARG_MAX**
> exec 函数参数的最大长度

**_NPROCESSORS_CONF**
> 已配置的处理器数量

**_NPROCESSORS_ONLN**
> 当前在线的处理器数量

# DESCRIPTION

**getconf** 检索由 POSIX 和系统特定扩展定义的系统配置变量。这些值代表系统限制和能力，应用程序可以查询它们以调整自身行为。

变量分为两类：系统级值（如 CHILD_MAX、PAGE_SIZE）和路径相关值（如 PATH_MAX、NAME_MAX），后者可能因文件系统而异。

对于需要查询系统限制而不想硬编码数值的 shell 脚本来说，这个命令很有用，可确保在不同系统之间的可移植性。

# CAVEATS

某些值可能是不确定的（显示为 "undefined"）。路径相关变量在不同文件系统上可能返回不同的值。并非所有系统都支持所有变量。

# HISTORY

getconf 是 POSIX 标准的一部分，自 20 世纪 90 年代初起就在类 Unix 系统上可用。它提供一种标准化的方式来查询 C 函数 sysconf()、pathconf() 和 confstr() 所返回的相同配置值。

# INSTALL

```apt: sudo apt install libc-bin```

```apk: sudo apk add musl-utils```

```nix: nix profile install nixpkgs#getconf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sysctl](/man/sysctl)(8), [ulimit](/man/ulimit)(1), [nproc](/man/nproc)(1)
