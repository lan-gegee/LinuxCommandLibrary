# TAGLINE

管理路由策略数据库，控制路由表查找的方式

# TLDR

显示**路由策略**数据库

```ip rule```

**添加**规则以查找特定表

```sudo ip rule add from all lookup [100]```

基于**源**地址添加规则

```sudo ip rule add from [192.168.1.0/24]```

基于**目标**地址添加规则

```sudo ip rule add to [10.0.0.0/8]```

**删除**一条规则

```sudo ip rule delete from [192.168.1.0/24]```

**清空**所有规则

```sudo ip rule flush```

将规则**保存**到文件

```ip rule save > [path/to/rules.dat]```

从文件**恢复**规则

```sudo ip rule restore < [path/to/rules.dat]```

# SYNOPSIS

**ip rule** [_command_] [_options_]

# PARAMETERS

**add** [_selector_] [_action_]
> 添加新规则

**delete** [_selector_]
> 移除一条规则

**flush**
> 删除所有规则

**save**
> 将规则输出到 stdout（用于备份）

**restore**
> 从 stdin 恢复规则

**from** _PREFIX_
> 匹配源地址

**to** _PREFIX_
> 匹配目标地址

**lookup** _TABLE_
> 要使用的路由表（编号或名称）

**priority** _NUM_
> 规则优先级（数值越小优先级越高）

# DESCRIPTION

**ip rule** 管理路由策略数据库（RPDB），它控制路由表查找的执行方式。规则定义选择器（条件）和动作（查询哪个表），从而实现基于策略的路由。

可以同时存在多个路由表，每个表包含不同的路由。规则根据源地址、目标地址、接口、防火墙标记等条件决定查询哪个表。这使得多宿主等复杂路由场景成为可能。

# CAVEATS

修改规则需要 root 权限。若无额外配置，规则更改在重启后不会保留。错误的规则可能破坏网络连接。

# HISTORY

策略路由作为高级路由能力的一部分在 Linux 2.2 中引入。iproute2 中的 ip rule 命令提供对这些功能的管理。

# INSTALL

```apt: sudo apt install iproute2```

```pacman: sudo pacman -S iproute2```

```apk: sudo apk add iproute2-minimal```

```zypper: sudo zypper install iproute2```

```brew: brew install iproute2```

```nix: nix profile install nixpkgs#iproute2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ip](/man/ip)(8), [ip-route](/man/ip-route)(8), [ip-route-add](/man/ip-route-add)(8)
