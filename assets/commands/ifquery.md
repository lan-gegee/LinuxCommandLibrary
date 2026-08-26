# TAGLINE

查询网络接口配置

# TLDR

**查询**某个接口的配置

```ifquery [eth0]```

**列出**所有已配置的接口

```ifquery --list```

列出当前**处于启用状态**的接口（来自状态文件）

```ifquery --state```

查询特定**类别**接口的配置（如 hotplug）

```ifquery --list --allow [hotplug]```

对照配置检查接口的**运行状态**

```ifquery --check [eth0]```

# SYNOPSIS

**ifquery** [_options_] _interface_

# PARAMETERS

_INTERFACE_
> 要查询的网络接口名称。

**-a**, **--all**
> 查询配置中标记为 **auto** 的所有接口。

**--list**
> 列出匹配的接口名称，而不是打印其配置。可与 **--all** 或 **--allow** 组合过滤。

**--state**
> 查询状态文件（**/run/network/ifstate**）中当前活动的接口，而非配置文件。

**--check**
> 将接口的运行状态与其配置进行比较并报告差异（仅限 ifupdown2）。

**--allow** _CLASS_
> 只匹配给定 allow 类别中的接口（如 **auto**、**hotplug**）。

**-i**, **--interfaces** _FILE_
> 从 _FILE_ 而不是 **/etc/network/interfaces** 读取配置。

**--force**
> 强制执行操作（在 ifupdown2 中与某些查询配合使用）。

**-V**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**ifquery** 查询 **/etc/network/interfaces** 及其 **interfaces.d/** 附加目录中定义的网络接口配置。它是只读的，从不修改接口状态。

不带 **--state** 调用时，它解析配置文件并打印与给定接口匹配的段落。使用 **--state** 时，它读取 **/run/network/ifstate** 以显示哪些接口当前被标记为启用。

在使用 **ifupdown2** 的系统上（较新的 Debian/Ubuntu 常见），还提供额外功能，包括用于比较运行状态与配置的 **--check** 以及 JSON 输出。

# CAVEATS

Debian/Ubuntu 特有；属于 **ifupdown**（或 **ifupdown2**）软件包。只读取配置和状态文件；绝不修改任何内容。**--check** 标志仅在 ifupdown2 中可用。使用 NetworkManager 或 systemd-networkd 的系统可能完全不使用 **/etc/network/interfaces**。

# INSTALL

```apt: sudo apt install ifupdown```

```apk: sudo apk add ifupdown-ng```

```nix: nix profile install nixpkgs#ifupdown-ng```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ifup](/man/ifup)(8), [ifdown](/man/ifdown)(8)
