# TAGLINE

Bitcoin Core 的图形界面

# TLDR

**启动 Bitcoin Core** 图形界面

```bitcoin-qt```

**在测试网上启动**

```bitcoin-qt -testnet```

**以指定的数据目录启动**

```bitcoin-qt -datadir=[/path/to/data]```

**限制连接数启动**

```bitcoin-qt -maxconnections=[8]```

**以修剪模式启动**以节省磁盘空间

```bitcoin-qt -prune=[550]```

**最小化启动**到系统托盘

```bitcoin-qt -min```

**不显示启动画面**

```bitcoin-qt -splash=0```

**重置 GUI 设置**

```bitcoin-qt -resetguisettings```

# SYNOPSIS

**bitcoin-qt** [_options_]

# DESCRIPTION

**bitcoin-qt** 是 Bitcoin Core（比特币协议的参考实现）的图形用户界面。它提供一个带钱包功能的完整比特币节点，以及用于发送、接收和管理比特币的友好界面。

运行 bitcoin-qt 会下载并验证整个比特币区块链（数百 GB）。它连接到比特币点对点网络，验证交易和区块，并将其转发给其他节点。

钱包功能包括地址生成、交易历史、币种控制（coin control）和手续费估算。它支持多钱包、只读监视地址和硬件钱包集成。

# PARAMETERS

**-datadir=** _path_
> 指定数据目录。

**-testnet**
> 使用测试网络。

**-regtest**
> 进入回归测试模式。

**-prune=** _n_
> 通过删除旧区块减少存储占用（单位 MB）。

**-maxconnections=** _n_
> 限制对等节点连接数。

**-proxy=** _ip:port_
> 通过 SOCKS5 代理连接。

**-onion=** _ip:port_
> 为 Tor 使用单独的代理。

**-listen**
> 接受传入连接。

**-server**
> 接受 JSON-RPC 命令。

**-rpcuser=** _user_
> RPC 用户名。

**-rpcpassword=** _pass_
> RPC 密码。

**-min**
> 最小化启动。

**-splash=** _0|1_
> 启动时显示启动画面。

**-resetguisettings**
> 将 GUI 设置重置为默认值。

**-choosedatadir**
> 启动时显示数据目录选择器。

**-lang=** _lang_
> 设置界面语言。

# CONFIGURATION

**~/.bitcoin/bitcoin.conf**
> Bitcoin Core 配置文件，用于网络、RPC、钱包和 GUI 设置。

# CAVEATS

初始区块链同步需要数小时至数天，取决于硬件和网络。完整节点需要 500+ GB 磁盘空间（或使用修剪模式）。同步和运行期间带宽占用较高。钱包文件（wallet.dat）应安全备份。在主网上运行涉及真实资金。

# HISTORY

**Bitcoin Core** 最初由 **中本聪（Satoshi Nakamoto）** 编写，于 **2009 年 1 月**作为第一个比特币实现发布。图形界面（bitcoin-qt）后来使用 Qt 框架添加。中本聪离开后，开发由 Gavin Andresen、Wladimir van der Laan 等首席维护者接续进行。它至今仍是定义比特币协议规则的参考实现。

# INSTALL

```pacman: sudo pacman -S bitcoin-qt```

```apk: sudo apk add bitcoin-qt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bitcoind](/man/bitcoind)(1), [bitcoin-cli](/man/bitcoin-cli)(1)
