# TAGLINE

Bitcoin Core 全节点守护进程

# TLDR

**启动**比特币守护进程

```bitcoind -daemon```

**以指定配置启动**

```bitcoind -conf=[bitcoin.conf]```

**停止**守护进程

```bitcoin-cli stop```

**在前台运行**

```bitcoind```

# SYNOPSIS

**bitcoind** [_options_]

# DESCRIPTION

**bitcoind** 是 Bitcoin Core 守护进程。它维护区块链的完整副本，验证交易和区块，并可充当钱包。该守护进程提供 RPC 和 REST 接口供交互使用。

运行全节点有助于比特币网络的去中心化，并允许以无需信任的方式验证交易。

# PARAMETERS

**-daemon**
> 作为后台守护进程运行

**-conf=**_file_
> 配置文件路径

**-datadir=**_dir_
> 数据目录

**-chain=**_chain_
> 选择链：main、testnet4、signet、regtest（默认：main）

**-testnet4**
> 使用 testnet4 网络

**-signet**
> 使用 signet 网络

**-regtest**
> 回归测试模式

**-prune=**_n_
> 启用修剪（仅保留 N MB）

**-txindex**
> 维护完整的交易索引

**-rpcuser=**_user_
> RPC 用户名

**-rpcpassword=**_pass_
> RPC 密码

**-rpcport=**_port_
> RPC 端口

**-server**
> 接受命令行和 JSON-RPC 命令

**-blocksonly**
> 不转发交易以降低带宽占用

# CONFIGURATION

**~/.bitcoin/bitcoin.conf**
> 主配置文件，用于守护进程模式、RPC 凭证、网络选择、修剪和索引选项。

# SYSTEM REQUIREMENTS

- **磁盘**: 约 600 GB+（完整区块链）
- **内存**: 最低 2 GB，建议 4 GB
- **网络**: 无限制或高流量额度
- **带宽**: 每月约 20 GB 上传

# FEATURES

- 完整的区块链验证
- 钱包功能
- 挖矿支持（通过外部矿机）
- RPC/REST API
- 修剪模式（减少存储占用）
- 支持 testnet/regtest
- ZMQ 通知

# WORKFLOW

```bash
# 启动守护进程
bitcoind -daemon

# 检查状态
bitcoin-cli getblockchaininfo

# 等待同步完成（可能需要数天）
bitcoin-cli getblockcount

# 停止守护进程
bitcoin-cli stop
```

# CAVEATS

初始同步需要数天或数周。需要较大磁盘空间（除非启用修剪）。带宽占用高。请妥善保管钱包备份。RPC 不应暴露到互联网。-testnet 标志（testnet3）已在 v28 中弃用并在 v30 中移除；请改用 -testnet4 或 -signet。

# HISTORY

**bitcoind** 由中本聪于 **2009 年**作为原始比特币软件的一部分创建，是比特币协议的参考实现。

# INSTALL

```apk: sudo apk add bitcoin```

```zypper: sudo zypper install bitcoind```

```brew: brew install bitcoin```

```nix: nix profile install nixpkgs#bitcoin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bitcoin-cli](/man/bitcoin-cli)(1), [bitcoin-qt](/man/bitcoin-qt)(1)
