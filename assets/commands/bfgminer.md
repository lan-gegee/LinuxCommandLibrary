# TAGLINE

模块化多线程比特币挖矿程序

# TLDR

**挖掘比特币**，使用带用户名和密码的矿池

```bfgminer -o [stratum+tcp://pool:port] -u [username] -p [password]```

**使用指定设备挖矿**

```bfgminer -o [stratum+tcp://pool:port] -u [username] -p [password] -d [device]```

**以 scrypt 算法挖矿**（Litecoin、Dogecoin 等）

```bfgminer --scrypt -o [stratum+tcp://pool:port] -u [username] -p [password]```

**设置 GPU 挖矿强度**

```bfgminer -o [stratum+tcp://pool:port] -u [username] -p [password] -I [10]```

**在指定端口启用 API**

```bfgminer -o [stratum+tcp://pool:port] -u [username] -p [password] --api-listen --api-port [4028]```

**从文件加载配置**

```bfgminer -c [path/to/config.json]```

# SYNOPSIS

**bfgminer** [_-DdEgIKklLmpPQqUSsTouvwOchV_] [_-o url_] [_-u user_] [_-p pass_]

# PARAMETERS

**-o**, **--url** _URL_
> 比特币 JSON-RPC 服务器的 URL（矿池地址）

**-u**, **--user** _USERNAME_
> JSON-RPC 服务器的用户名

**-p**, **--pass** _PASSWORD_
> JSON-RPC 服务器的密码

**-O**, **--userpass** _USER:PASS_
> 服务器的用户名:密码对

**-d**, **--device** _PATTERN_
> 启用匹配模式（pattern）的设备（用 -d? 列出）

**-I**, **--intensity** _VALUE_
> GPU 扫描强度（-10 到 20，默认：d 表示桌面交互优先）

**--scrypt**
> 使用 scrypt 算法而不是 SHA256d

**-c**, **--config** _FILE_
> 加载 JSON 格式的配置文件

**-l**, **--log** _INTERVAL_
> 日志输出的时间间隔（秒）

**-L**, **--log-file** _FILE_
> 将日志输出追加到该文件

**-T**, **--text-only**
> 禁用 ncurses 格式化的屏幕输出

**-q**, **--quiet**
> 禁用日志输出，仅显示状态和错误

**--api-listen**
> 启用 API（默认：禁用）

**--api-port** _PORT_
> API 端口（默认：4028）

**--api-allow** _[G:]IP[/PREFIX]_
> 仅允许指定地址访问 API

**--failover-only**
> 在多矿池配置下不把工作泄漏给备用矿池

**-U**, **--quota** _VALUE_
> 矿池的负载均衡配额（例如 2:http://pool）

**--benchmark**
> 以离线基准测试模式运行

**--shares** _NUMBER_
> 挖到指定数量的份额后退出

**-V**, **--version**
> 显示版本并退出

**-h**, **--help**
> 显示帮助信息并退出

# DESCRIPTION

**bfgminer** 是一个用 C 编写的模块化多线程挖矿程序，设计用于挖掘 Bitcoin 及其他基于 SHA256d 或 scrypt 的加密货币。它支持多种硬件，包括 ASIC、FPGA、GPU 和 CPU。

该挖矿程序通过 stratum 协议或 JSON-RPC 连接矿池并提交工作量证明结果。它支持自动检测和配置受支持的挖矿设备，并为兼容的硬件提供动态调频、监控和风扇转速控制。

BFGMiner 内置用于远程监控和控制的 API，适合管理矿机。它支持多个同时工作的矿池，并提供可配置的故障转移与负载均衡策略。

# CAVEATS

由于 ASIC 矿机占主导地位，GPU 挖掘 Bitcoin 已不再有利可图。BFGMiner 的 GPU 支持主要用于基于 scrypt 的币种或测试。该软件需要为你的挖矿硬件安装合适的驱动。ASIC 和 FPGA 设备可能需要特定固件。运行挖矿软件会显著增加功耗和发热。

# HISTORY

BFGMiner 由 Luke Dashjr 于 **2012 年**从 **CGMiner** 分叉而来，专注于 FPGA 和 ASIC 支持并保持模块化。其名称是 "**B**asically a **F**reaking **G**ood Miner" 的首字母缩略词。它凭借广泛的硬件支持和远程 API 功能而流行。开发仍在 GitHub 上继续，支持现代挖矿硬件。

# SEE ALSO

[cgminer](/man/cgminer)(1), [xmrig](/man/xmrig)(1)
