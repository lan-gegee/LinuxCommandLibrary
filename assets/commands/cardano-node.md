# TAGLINE

Cardano 区块链网络的核心节点软件

# TLDR

**在主网上运行 Cardano 节点**

```cardano-node run --topology [path/to/topology.json] --database-path [path/to/db] --socket-path [path/to/node.socket] --config [path/to/config.json]```

**以指定的主机和端口运行节点**

```cardano-node run --topology [topology.json] --database-path [db/] --socket-path [node.socket] --host-addr [127.0.0.1] --port [3001] --config [config.json]```

**带密钥运行出块节点**

```cardano-node run --topology [topology.json] --database-path [db/] --socket-path [node.socket] --config [config.json] --shelley-kes-key [kes.skey] --shelley-vrf-key [vrf.skey] --shelley-operational-certificate [node.cert]```

**作为中继节点运行**（不出块）

```cardano-node run --non-producing-node --topology [topology.json] --database-path [db/] --socket-path [node.socket] --config [config.json]```

**运行前校验数据库**

```cardano-node run --validate-db --topology [topology.json] --database-path [db/] --socket-path [node.socket] --config [config.json]```

# SYNOPSIS

**cardano-node** run [_options_]

**cardano-node** --version

**cardano-node** --help

# PARAMETERS

**--topology** _FILEPATH_
> 描述网络对等节点的 topology.json 文件路径

**--database-path** _FILEPATH_
> 存储区块链状态的目录

**--socket-path** _FILEPATH_
> 用于 IPC 通信的 Unix 域套接字路径

**--config** _FILEPATH_
> 节点配置 JSON 文件路径

**--host-addr** _IPV4_
> 绑定以接受传入连接的 IPv4 地址

**--host-ipv6-addr** _IPV6_
> 绑定以接受传入连接的 IPv6 地址

**--port** _PORT_
> 监听对等连接的端口号

**--shelley-kes-key** _FILEPATH_
> 用于出块的 KES（Key Evolving Signature）签名密钥路径

**--shelley-vrf-key** _FILEPATH_
> VRF（Verifiable Random Function）签名密钥路径

**--shelley-operational-certificate** _FILEPATH_
> 权益池操作证书路径

**--non-producing-node**
> 即使指定了凭证也作为中继节点启动

**--validate-db**
> 启动时校验所有数据库文件

**--shutdown-on-slot-synced** _SLOT_
> 同步到指定槽位号后关机

**--shutdown-on-block-synced** _BLOCK_
> 同步到指定区块号后关机

**--shutdown-ipc** _FD_
> 当继承的文件描述符到达 EOF 时关机

**-h**, **--help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**cardano-node** 是 Cardano 区块链网络的核心组件，实现了 Ouroboros 共识协议。它维护区块链的本地副本，验证交易，并参与点对点网络。

节点可以两种模式运行：作为转发交易和区块的中继节点，或者作为按协议被选中时创建新区块的出块节点（权益池）。出块节点需要 KES 密钥、VRF 密钥和操作证书。

与节点的通信通过 **--socket-path** 指定的 Unix 域套接字进行。**cardano-cli** 工具和其他应用程序使用 **CARDANO_NODE_SOCKET_PATH** 环境变量来定位该套接字，以进行查询和提交交易。

# CONFIGURATION

**config.json**
> 主节点配置文件，指定协议参数、日志记录、追踪和网络设置。

**topology.json**
> 定义节点要连接的网络对等节点，包括中继节点和出块节点。

# CAVEATS

运行完整节点需要大量磁盘空间（主网超过 100GB）和内存。初始同步可能耗费数小时，取决于硬件和网络速度。运营权益池期间节点必须保持运行并联网。配置文件必须与你打算连接的网络（mainnet、preprod、preview）相匹配。

# HISTORY

cardano-node 由 **Input Output Global (IOG)**（前身 IOHK）开发，属于 Charles Hoskinson 创立的 Cardano 区块链项目的一部分。该项目于 **2017 年 9 月**以 Byron era 启动主网。主要升级包括 **2020 年**引入质押与去中心化的 **Shelley** era、**2021 年**加入智能合约的 **Alonzo**，以及延续至 Basho 和 Voltaire eras 的持续开发。该节点用 **Haskell** 编写，实现了经过同行评审的密码学协议。

# INSTALL

```aur: yay -S cardano-node```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cardano-cli](/man/cardano-cli)(1), [cardano-wallet](/man/cardano-wallet)(1)
