# TAGLINE

检查网络链路状态

# TLDR

**查看接口状态**

```mii-tool [eth0]```

**查看所有接口**

```mii-tool```

**详细输出**

```mii-tool -v [eth0]```

**监视状态**

```mii-tool -w [eth0]```

**强制速率**

```mii-tool -F [100baseTx-FD] [eth0]```

**重置接口**

```mii-tool -R [eth0]```

# SYNOPSIS

**mii-tool** [_options_] [_interface_]

# PARAMETERS

_INTERFACE_
> 网络接口。

**-v**
> 详细输出。

**-w**
> 监视变化。

**-F** _MEDIA_
> 强制介质类型。

**-R**
> 重新开始协商。

**-A** _MEDIA,MEDIA,..._
> 自动协商时仅宣告指定的介质类型。

**-V**
> 显示版本信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mii-tool** 检查网络链路状态。它显示速率、双工模式和链路状态。

该工具使用 MII（Media Independent Interface，介质无关接口）查询以太网适配器。支持的介质类型包括 100baseT4、100baseTx-FD、100baseTx-HD、10baseT-FD 和 10baseT-HD。

# CAVEATS

已弃用，请使用 ethtool。并非适用于所有适配器。需要 root 权限。

# HISTORY

mii-tool 是 **net-tools** 中用于检查以太网链路状态的工具，现已被 ethtool 取代。

# INSTALL

```apt: sudo apt install net-tools```

```dnf: sudo dnf install net-tools```

```pacman: sudo pacman -S net-tools```

```apk: sudo apk add mii-tool```

```zypper: sudo zypper install net-tools```

```brew: brew install net-tools```

```nix: nix profile install nixpkgs#net-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ethtool](/man/ethtool)(8), [ifconfig](/man/ifconfig)(8), [ip](/man/ip)(8)
