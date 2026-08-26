# TAGLINE

面向 ASIC 设备的多线程加密货币挖矿程序

# TLDR

使用矿池**挖掘比特币**，附带用户名和密码

```cgminer -o [stratum+tcp://pool:port] -u [username] -p [password]```

对接本地比特币节点**单独挖矿**

```cgminer -o [http://localhost:8332] -u [rpcuser] -p [rpcpassword] --btc-address [your_address]```

以**基准测试模式运行**而不提交份额

```cgminer --benchmark```

在指定端口**启用 API**

```cgminer -o [stratum+tcp://pool:port] -u [username] -p [password] --api-listen --api-port [4028]```

**从文件加载配置**

```cgminer -c [path/to/config.json]```

使用**多个矿池**进行负载均衡挖矿

```cgminer -o [pool1:port] -u [user1] -p [pass1] -o [pool2:port] -u [user2] -p [pass2] --load-balance```

# SYNOPSIS

**cgminer** [_-DdlmpPqUTouOchnV_] [_-o url_] [_-u user_] [_-p pass_]

# PARAMETERS

**-o**, **--url** _URL_
> 比特币 JSON-RPC 服务器 URL（矿池或本地节点）

**-u**, **--user** _USERNAME_
> JSON-RPC 服务器的用户名

**-p**, **--pass** _PASSWORD_
> JSON-RPC 服务器的密码

**-O**, **--userpass** _USER:PASS_
> 服务器的用户名:密码对

**-c**, **--config** _FILE_
> 加载 JSON 格式的配置文件

**--benchmark**
> 以基准测试模式运行，不产生实际份额

**--shares** _NUMBER_
> 挖到指定数量的份额后退出

**--no-submit-stale**
> 若份额被检测为过期则不提交

**--btc-address** _ADDRESS_
> 单独挖矿时接收 coinbase 奖励的比特币地址

**--balance**
> 将矿池策略改为均衡份额分配

**--load-balance**
> 将矿池策略改为基于配额的均衡

**--rotate** _MINUTES_
> 每 N 分钟在矿池之间轮换

**--failover-only**
> 主矿池活跃时不向备用矿池泄漏工作

**--api-listen**
> 启用挖矿 API（默认禁用）

**--api-port** _PORT_
> API 端口号（默认：4028）

**--api-allow** _[G:]IP[/PREFIX]_
> 仅允许给定地址访问 API

**-D**, **--debug**
> 启用调试输出

**-l**, **--log** _INTERVAL_
> 日志输出间隔，单位为秒（默认：5）

**-q**, **--quiet**
> 禁用日志输出，仅显示状态和错误

**-T**, **--text-only**
> 禁用 ncurses 格式化的屏幕输出

**--temp-cutoff** _TEMP_
> 设备将被停用的温度阈值

**--usb** _DEVICES_
> USB 设备选择（如 1:2,1:3 或 BAS:1,BFL:1）

**-h**, **--help**
> 打印帮助信息并退出

**-V**, **--version**
> 显示版本并退出

# DESCRIPTION

**cgminer** 是一款用于比特币及其他 SHA256d 加密货币的多线程多矿池挖矿程序。它最初同时支持 CPU、GPU、FPGA 和 ASIC 挖矿；由于 GPU 挖掘比特币已不再有经济可行性，现代版本专注于 ASIC 设备。

该程序支持多个矿池，并提供可配置的故障转移、负载均衡和轮换策略。它通过 stratum 协议或 JSON-RPC 连接并提交工作量证明解。内置 API 支持远程监控和控制挖矿操作。

CGMiner 支持多种 ASIC 硬件，包括 Avalon、AntMiner、BitFury、Cointerra、Drillbit、HashFast、Icarus 和 Klondike 设备。在 Linux 上直接支持 USB 而无需额外驱动，不过非 root 访问可能需要配置 udev 规则。

# CONFIGURATION

**cgminer.conf**
> JSON 配置文件，包含矿池 URL、凭证、设备设置和挖矿参数。可通过 -c 标志加载，或从工作目录自动加载。

# CAVEATS

由于对比特币而言已无利可图，近期版本移除了 GPU 挖矿支持。在 Linux 上，USB 设备权限可能需要将用户加入 **plugdev** 组或安装 cgminer 发行版附带的 udev 规则。高算力会产生大量热量和功耗。矿池 URL 必须使用正确的协议前缀（单独挖矿用 **http://**，矿池挖矿用 **stratum+tcp://**）。

# HISTORY

CGMiner 由 **Con Kolivas** (ckolivas) 开发，首发于 **2011 年**。它最初是 Jeff Garzik 的 CPU 挖矿程序 **cpuminer** 的分支。名字意为 **Con's GPU Miner**，后来扩展支持 FPGA 和 ASIC。在 GPU 挖矿和早期 ASIC 挖矿时代，它是最广泛使用的比特币挖矿程序之一。BFGMiner 于 2012 年从 CGMiner 分叉而来，专注于 FPGA/ASIC 的模块化。

# INSTALL

```nix: nix profile install nixpkgs#cgminer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bfgminer](/man/bfgminer)(1), [xmrig](/man/xmrig)(1)
