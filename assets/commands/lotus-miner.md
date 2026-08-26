# TAGLINE

Filecoin 存储提供商 CLI

# TLDR

**初始化新的矿工**

```lotus-miner init```

**启动矿工守护进程**

```lotus-miner run```

**查看矿工状态**

```lotus-miner info```

**列出存储交易**

```lotus-miner storage-deals list```

**查看扇区状态**

```lotus-miner sectors status [sectorNumber]```

# SYNOPSIS

**lotus-miner** [_command_] [_options_]

# PARAMETERS

**init**
> 初始化新的存储矿工。

**run**
> 启动存储矿工守护进程。

**info**
> 显示矿工信息与状态。

**stop**
> 停止正在运行的矿工守护进程。

**config**
> 管理矿工配置。

**storage-deals**
> 管理存储交易。

**sectors**
> 管理和检查扇区。

**auth**
> 管理 RPC 认证令牌。

**backup**
> 创建元数据备份。

**--help**, **-h**
> 显示帮助。

**--version**, **-v**
> 输出版本。

# DESCRIPTION

**lotus-miner** 是 **Lotus** Filecoin 实现中的存储提供商组件。它管理存储交易的生命周期、扇区封装和证明生成，用于以存储提供商的身份参与 Filecoin 网络。

矿工与运行中的 **lotus** 守护进程（全节点）通信，负责抵押存储容量、接受客户端的存储交易，以及向区块链提交存储证明。

# CAVEATS

需要运行中的 **lotus** 全节点守护进程。存储挖矿需要大量磁盘空间、用于生成证明的 GPU，以及已抵押的 FIL 余额。使用 Go 编写。

# SEE ALSO

[geth](/man/geth)(1), [ipfs](/man/ipfs)(1)
