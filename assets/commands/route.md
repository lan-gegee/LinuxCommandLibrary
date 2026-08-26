# TAGLINE

显示和管理 IP 路由表

# TLDR

**以数字地址格式显示路由表**

```route -n```

**添加默认网关**

```sudo route add default gw [192.168.1.1]```

**添加到网络的路由**

```sudo route add -net [10.0.0.0] netmask [255.0.0.0] gw [192.168.1.1]```

**添加到主机的路由**

```sudo route add -host [192.168.2.100] gw [192.168.1.1]```

**添加 IPv6 路由**

```sudo route -6 add [2001:db8::/32] gw [fe80::1] dev [eth0]```

**删除到网络的路由**

```sudo route del -net [10.0.0.0] netmask [255.0.0.0]```

**删除默认网关**

```sudo route del default```

**添加 reject 路由以阻止发往某网络的流量**

```sudo route add -net [10.0.0.0] netmask [255.0.0.0] reject```

# SYNOPSIS

**route** [**-CFvnNee**] [**-A** _family_|**-4**|**-6**]

**route** [**-v**] [**-A** _family_|**-4**|**-6**] **add**|**del** [**-net**|**-host**] _target_ [**netmask** _mask_] [**gw** _gateway_] [**metric** _N_] [**mss** _M_] [**window** _W_] [**irtt** _I_] [**reject**] [**dev** _interface_]

**route** [**-V**|**--version**] [**-h**|**--help**]

# PARAMETERS

**-n**
> 显示数字地址而不解析主机名；避免 DNS 查询，加快显示速度

**-v**
> 详细输出

**-e**
> 以 **netstat**(8) 格式显示路由表；使用 **-ee** 可获得包含 MTU、window 和 irtt 列的扩展输出

**-C**
> 操作内核路由缓存而非 FIB

**-N**
> 显示符号形式的网络名而非 CIDR 表示法（与 **-n** 相反）

**-4**
> 操作 IPv4 路由（**-A inet** 的别名）

**-6**
> 操作 IPv6 路由（**-A inet6** 的别名）

**-A** _family_
> 指定地址族（例如 **inet**、**inet6**）

**-F**
> 操作内核 FIB（转发信息库）路由表（默认）

**-V**, **--version**
> 显示版本信息

**add**
> 添加新路由

**del**
> 删除路由

**-net**
> 目标是网络地址

**-host**
> 目标是单个主机地址

**gw** _gateway_
> 经由指定网关路由数据包；该网关必须是已可达的

**netmask** _mask_
> 为网络路由指定子网掩码

**dev** _interface_
> 强制将该路由关联到指定的网络接口

**metric** _N_
> 为路由设置度量值（优先级）；数值越小越优先

**mss** _M_
> 为使用此路由的连接设置 TCP 最大段大小（MSS），单位为字节

**window** _W_
> 为使用此路由的连接设置 TCP 窗口大小，单位为字节

**irtt** _I_
> 设置 TCP 用于此路由的初始往返时间，单位为毫秒（1–12000）

**reject**
> 安装一条阻塞路由，使查找失败并返回 "Network unreachable"；可用于阻止发往特定目的地的流量

**mod**, **dyn**, **reinstate**
> 由路由守护进程设置的诊断标志，用于标记动态或修改过的路由；通常不会手动使用

# DESCRIPTION

**route** 用于显示和操作内核 IP 路由表。内核利用路由表根据数据包的目的地址决定将其发送到哪里。

不带参数时，**route** 显示当前路由表。**-n** 标志以数字形式显示地址，避免 DNS 查询，从而加快显示速度。

可以为网络（一段地址范围）或特定主机添加路由。默认路由（IPv4 中为 0.0.0.0/0）处理不匹配任何更具体路由的流量——通常指向互联网网关。

在添加经由某网关的新路由之前，用 **gw** 指定的网关必须已经能够通过现有路由直接到达。目标支持 CIDR 前缀表示法（例如 **10.0.0.0/8**），效果等同于使用 **netmask** 来指定目标。

现代 Linux 系统更推荐使用 iproute2 软件包中的 **ip route**，但 **route** 出于兼容性考虑仍然可用，老系统上的管理员对它非常熟悉。

# OUTPUT COLUMNS

**Destination**：目标网络或主机地址

**Gateway**：下一跳网关地址；`*` 表示目的地可直接到达（无需网关）

**Genmask**：目的地的子网掩码；主机路由为 `255.255.255.255`，默认路由为 `0.0.0.0`

**Flags**：路由状态标志 — **U**=启用、**H**=主机路由、**G**=经由网关、**R**=已恢复、**D**=动态安装、**M**=已被路由守护进程修改、**A**=由 addrconf 安装、**!=**=拒绝路由

**Metric**：到目标的距离，通常以跳数计；当多条路由匹配时，数值越小越优先

**Ref**：对该路由的引用数量（Linux 中未使用；始终为 0）

**Use**：路由查找次数

**Iface**：用于在此路由上发送数据包的网络接口

# CAVEATS

使用 **route** 所做的路由更改在重启后不会保留。如需永久路由，请使用网络配置文件或网络管理器（如 NetworkManager 或 systemd-networkd）。

**route** 命令已被弃用，建议改用 iproute2 软件包中的 **ip route**，后者功能更多且语法一致。

在添加经由某网关的路由之前，该网关必须是可达的；如有必要，先建立一条到网关的直接路由。

修改路由需要 root 权限。错误的路由配置可能导致网络连接完全中断。

# INSTALL

```apt: sudo apt install net-tools```

```dnf: sudo dnf install net-tools```

```pacman: sudo pacman -S net-tools```

```apk: sudo apk add net-tools```

```zypper: sudo zypper install net-tools```

```brew: brew install net-tools```

```nix: nix profile install nixpkgs#net-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ip](/man/ip)(8), [ip-route](/man/ip-route)(8), [ifconfig](/man/ifconfig)(8), [netstat](/man/netstat)(8), [traceroute](/man/traceroute)(8)
