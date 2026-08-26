# TAGLINE

支持 SPV 验证的轻量级比特币钱包

# TLDR

**启动 Electrum 图形界面**

```electrum```

**创建新钱包**

```electrum create```

**获取钱包余额**

```electrum getbalance```

**列出钱包中的所有地址**

```electrum listaddresses```

**生成新的接收地址**

```electrum createnewaddress```

**向某个地址发送比特币**

```electrum payto [address] [amount]```

**启动守护进程**以便后台运行

```electrum daemon start```

**在守护进程中加载指定钱包**

```electrum load_wallet -w [path/to/wallet]```

# SYNOPSIS

**electrum** [_options_] [_command_] [_args_]

**electrum** daemon [_start_|_stop_|_status_]

**electrum** [_-w wallet_] _command_

# PARAMETERS

**-w**, **--wallet** _PATH_
> 使用指定路径的钱包

**-o**, **--offline**
> 以离线模式运行，不访问网络

**-g**, **--gui** _GUI_
> 选择用户界面（qt、text）

**-s**, **--server** _HOST:PORT:PROTOCOL_
> 设置服务器地址

**-p**, **--proxy** _TYPE:HOST:PORT_
> 设置代理服务器

**-v**, **--verbose**
> 显示调试信息

**-P**, **--portable**
> 使用便携钱包模式

**-L**, **--lang** _LANGUAGE_
> 设置 GUI 的默认语言

**--testnet**
> 使用比特币测试网

**--mainnet**
> 使用比特币主网（默认）

**-a**, **--all**
> 显示所有地址

**-h**, **--help**
> 显示帮助消息并退出

**--version**
> 显示程序版本

# COMMANDS

**create**
> 创建新钱包

**restore**
> 从种子恢复钱包

**getbalance**
> 显示钱包余额

**listaddresses**
> 列出所有钱包地址

**createnewaddress**
> 生成新的接收地址

**getaddresshistory** _ADDRESS_
> 显示某地址的交易历史

**history**
> 显示钱包交易历史

**payto** _ADDRESS_ _AMOUNT_
> 创建并发送一笔交易

**broadcast** _TX_
> 广播已签名的交易

**signmessage** _ADDRESS_ _MESSAGE_
> 用某个地址对消息签名

**verifymessage** _ADDRESS_ _SIGNATURE_ _MESSAGE_
> 验证已签名的消息

**commands**
> 列出所有可用命令

# DESCRIPTION

**electrum** 是一个轻量级比特币钱包，它连接远程服务器而不是下载整条区块链。它同时支持图形界面和命令行操作，既适合桌面使用，也适合脚本化自动化。

该钱包使用由助记词种子短语生成的分层确定性（HD）密钥，仅凭种子即可完整恢复钱包。它支持多重签名钱包、硬件钱包集成（Trezor、Ledger）以及只读观察钱包。

对于命令行操作，守护进程可以在后台运行并处理网络通信，CLI 命令则与它交互。某些命令使用 **-o** 标志即可在无守护进程的情况下离线工作。特殊参数 **!** 表示"可用最大金额"，**-** 表示从 stdin 读取。

# CONFIGURATION

**~/.electrum/config**
> 主配置文件，包含钱包设置和服务器偏好。

**~/.electrum/wallets/**
> 存放加密钱包文件的目录。

**~/.electrum/daemon**
> 守护进程套接字和进程信息。

# CAVEATS

Electrum 连接的第三方服务器可以看到你的地址和交易历史，但无法访问你的资金。要获得最大隐私，请运行自己的 Electrum 服务器。钱包文件默认加密，但仍应安全备份。硬件钱包集成需要额外的软件包。

# HISTORY

Electrum 由 **Thomas Voegtlin** 创建，于 **2011 年 11 月**首次发布。它是最早的轻量级比特币钱包之一，开创了结合远程服务器的 SPV（简化支付验证）。其名字来自拉丁语的"琥珀"，因为琥珀摩擦会产生静电。Electrum 引入了用于钱包备份的助记词概念，后来成为整个加密货币行业的标准。

# INSTALL

```dnf: sudo dnf install electrum```

```pacman: sudo pacman -S electrum```

```apk: sudo apk add electrum```

```nix: nix profile install nixpkgs#electrum```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bitcoin-cli](/man/bitcoin-cli)(1), [trezorctl](/man/trezorctl)(1)

# RESOURCES

```[Source code](https://github.com/spesmilo/electrum)```

```[Homepage](https://electrum.org/)```

```[Documentation](https://electrum.readthedocs.io/)```

<!-- verified: 2026-07-14 -->
