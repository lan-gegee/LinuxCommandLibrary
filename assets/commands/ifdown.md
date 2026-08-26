# TAGLINE

停用之前由 ifup 配置的网络接口

# TLDR

**禁用**指定接口

```ifdown [eth0]```

**禁用所有**已启用的接口

```ifdown -a```

只**显示**要执行的命令而不运行（干跑）

```ifdown -n [eth0]```

即使接口状态显示为已停止，也**强制**解除配置

```ifdown --force [eth0]```

**详细**输出

```ifdown -v [eth0]```

使用**其他** interfaces 文件

```ifdown -i [/path/to/interfaces] [eth0]```

# SYNOPSIS

**ifdown** [_options_] _interface_

# PARAMETERS

**-a**, **--all**
> 作用于所有已定义的接口，按状态文件中列出的顺序依次停用。

**--allow** _CLASS_
> 只作用于在 /etc/network/interfaces 中列于某个 `allow-CLASS` 段落中的接口（如 `allow-hotplug`）。

**-i** _FILE_, **--interfaces**=_FILE_
> 从 _FILE_ 而不是 /etc/network/interfaces 读取接口定义。

**--state-dir**=_DIR_
> 将接口状态保存在 _DIR_ 而不是 /run/network。

**-X** _PATTERN_, **--exclude**=_PATTERN_
> 排除匹配 _PATTERN_ 的接口。

**-o** _OPTION=VALUE_
> 将 _OPTION_ 设置为 _VALUE_，如同定义在 /etc/network/interfaces 中一样。

**-n**, **--no-act**
> 不配置任何接口，也不运行 up/down 命令（干跑）。

**-v**, **--verbose**
> 在命令执行时显示它们。

**-f**, **--force**
> 即使 ifupdown 认为接口未处于启用状态也强制解除配置。

**--ignore-errors**
> 即使某个命令或脚本失败也继续执行。

**--no-mappings**
> 解除配置时不运行映射（mappings）。

**--no-scripts**
> 不运行 /etc/network/if-*.d/ 下的任何脚本。

**-V**, **--version**
> 显示版权和版本信息。

**-h**, **--help**
> 显示选项摘要。

# DESCRIPTION

**ifdown** 停用之前由 ifup 配置的网络接口。它从 **/etc/network/interfaces** 读取接口定义，并执行相应的命令和脚本来解除接口配置。

该命令会完成一切必要的清理工作，包括移除 IP 地址、停止 DHCP 客户端以及运行 interfaces 文件中定义的用户脚本。

# CAVEATS

属于 ifupdown 软件包，主要用于基于 Debian 的系统。现代系统通常改用 NetworkManager 或 systemd-networkd。接口必须先由 ifup 启用过，ifdown 才能正常工作。

# HISTORY

ifdown 属于 ifupdown 软件包——Debian 及其衍生版传统的网络接口配置系统。它自 Debian 早期就开始使用，但在桌面系统上正逐渐被 NetworkManager 取代，在服务器上则被 systemd-networkd 取代。

# INSTALL

```apt: sudo apt install ifupdown```

```apk: sudo apk add ifupdown-ng```

```nix: nix profile install nixpkgs#ifupdown-ng```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ifup](/man/ifup)(8), [ip](/man/ip)(8)
