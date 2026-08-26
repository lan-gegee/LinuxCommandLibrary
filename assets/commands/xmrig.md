# TAGLINE

加密货币挖矿软件

# TLDR

使用钱包地址**挖矿到矿池**

```xmrig -o [pool.example.com:3333] -u [wallet_address]```

**使用配置文件挖矿**

```xmrig --config [config.json]```

**运行基准测试**

```xmrig --bench [1M]```

**以指定 CPU 线程数挖矿**

```xmrig -o [pool:port] -u [wallet] -t [4]```

**在后台运行**

```xmrig -o [pool:port] -u [wallet] -B```

**启用 CUDA**（NVIDIA GPU）

```xmrig -o [pool:port] -u [wallet] --cuda```

**启用 OpenCL**（AMD GPU）

```xmrig -o [pool:port] -u [wallet] --opencl```

**试运行（dry run）**测试配置

```xmrig --config [config.json] --dry-run```

# SYNOPSIS

**xmrig** [_options_]

**xmrig** -o _pool_ -u _wallet_ [_options_]

# PARAMETERS

**-o** _URL_, **--url** _URL_
> 矿池 URL（host:port）

**-u** _WALLET_, **--user** _WALLET_
> 钱包地址或用户名

**-p** _PASS_, **--pass** _PASS_
> 矿池密码

**-t** _NUM_, **--threads** _NUM_
> CPU 线程数量

**-c** _FILE_, **--config** _FILE_
> JSON 配置文件

**-B**, **--background**
> 在后台运行（守护进程模式）

**--cuda**
> 启用 CUDA 后端（NVIDIA）

**--opencl**
> 启用 OpenCL 后端（AMD）

**--no-cpu**
> 禁用 CPU 挖矿

**--cuda-devices** _LIST_
> 以逗号分隔的 CUDA 设备索引

**--opencl-devices** _LIST_
> 以逗号分隔的 OpenCL 设备索引

**--donate-level** _N_
> 捐赠百分比（默认：1%）

**--randomx-1gb-pages**
> 使用 1 GB 大页（Linux，需要预先设置）

**--bench** _N_
> 运行基准测试（1M 到 10M 次哈希）

**--stress**
> 持续压力测试模式

**--dry-run**
> 测试配置而不实际挖矿

**-V**, **--version**
> 显示版本

**-h**, **--help**
> 显示帮助

# DESCRIPTION

**xmrig** 是一个高性能加密货币挖矿软件，支持 RandomX（Monero）、KawPow（Ravencoin）、CryptoNight 和 GhostRider 算法。它支持在 Windows、Linux、macOS 和 FreeBSD 上进行 CPU 和 GPU 挖矿。

配置最好通过 JSON 配置文件完成，它支持命令行无法实现的特性，例如多个矿池和挖矿方案（mining profile）。挖矿程序会根据硬件检测自动选择最优设置。

在 Linux 上进行 RandomX 挖矿时，启用大页内存可以显著提升性能。该挖矿程序默认包含 1% 的开发者捐赠，可通过配置调整。

# CAVEATS

加密货币挖矿耗电量大并产生热量。收益取决于硬件、电费和加密货币价格。一些云服务商和 ISP 禁止挖矿。满负荷运行可能缩短硬件寿命。持续运行请确保散热充足。

# HISTORY

XMRig 作为一个开源 Monero 挖矿软件而创建，最初专注于使用 CryptoNight 算法的 CPU 挖矿。当 Monero 于 **2019** 年切换到 RandomX 算法时，XMRig 也随之更新以提供支持。该项目随后通过 CUDA 和 OpenCL 后端扩展了 GPU 支持。凭借其性能、跨平台支持和活跃的开发，XMRig 成为使用最广泛的挖矿软件之一。

# INSTALL

```apt: sudo apt install xmrig```

```pacman: sudo pacman -S xmrig```

```apk: sudo apk add xmrig```

```zypper: sudo zypper install xmrig```

```brew: brew install xmrig```

```nix: nix profile install nixpkgs#xmrig```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cgminer](/man/cgminer)(1), [bfgminer](/man/bfgminer)(1)
