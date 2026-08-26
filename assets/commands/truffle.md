# TAGLINE

以太坊智能合约开发框架

# TLDR

初始化项目

```truffle init```

编译合约

```truffle compile```

运行迁移

```truffle migrate```

运行测试

```truffle test```

启动控制台

```truffle console```

部署到网络

```truffle migrate --network [mainnet]```

启动开发区块链

```truffle develop```

创建新的合约样板

```truffle create contract [ContractName]```

创建新的迁移脚本

```truffle create migration [MigrationName]```

运行指定的测试文件

```truffle test [test/MyContract.test.js]```

启用优化器编译

```truffle compile --all```

# SYNOPSIS

**truffle** _command_ [_--network network_] [_options_]

# PARAMETERS

**init**
> 初始化项目。

**compile**
> 编译合约。

**migrate**
> 部署合约。

**test**
> 运行测试。

**console**
> 交互式控制台。

**develop**
> 本地区块链。

**create** _TYPE_ _NAME_
> 生成新的合约、迁移或测试样板。

**unbox** _box_name_
> 下载预构建的 Truffle 项目 (Truffle Box)。

**networks**
> 显示各网络上已部署合约的地址。

**debug** _txHash_
> 以交互方式调试一笔交易。

**--network** _NAME_
> 目标网络（在 truffle-config.js 中定义）。

**--reset**
> 从头重新执行所有迁移。

**--compile-all**
> 即使未更改也重新编译所有合约。

**--verbose-rpc**
> 记录与以太坊客户端的 RPC 通信。

# DESCRIPTION

**Truffle** 是一个以太坊智能合约开发框架，提供从编译到部署和测试的完整工作流。它将 Solidity 合约编译为字节码和 ABI 工件，通过有序的迁移脚本管理部署，并支持 JavaScript 和 Solidity 两套测试套件。

内置的开发区块链 (truffle develop) 提供了一个本地以太坊环境，交易即时确认且账户预充值，开发期间无需支付 gas 费用。交互式控制台可以连接任何已配置的网络，并与已部署的合约直接交互。

项目采用标准目录结构组织，包括 contracts、migrations 和 test 目录。truffle-config.js 中的网络配置定义了从本地开发环境到公共测试网和主网的各类部署目标。

# CONFIGURATION

**truffle-config.js**
> 主项目配置文件，定义网络端点、编译器设置和迁移选项。

**contracts/**
> 存放 Solidity 智能合约源文件的目录。

**migrations/**
> 存放按序号顺序执行的部署脚本的目录。

# CAVEATS

**Truffle 已于 2023 年 9 月停止维护**，不再积极开发；建议迁移到 Hardhat。需要 Node.js (v12 或更高版本)。部署到主网会产生真实的 gas 费用。可通过 `npm install -g truffle` 安装。

# HISTORY

**Truffle** 由 **Tim Coulter** 创建，后来由 **ConsenSys** 作为 Truffle Suite 的一部分维护。它曾是多年来占主导地位的以太坊开发框架。ConsenSys 于 **2023 年 9 月**宣布 **Truffle 停止维护**，推荐迁移到 Hardhat 或其他仍在活跃维护的框架。

# INSTALL

```brew: brew install truffle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hardhat](/man/hardhat)(1), [ganache](/man/ganache)(1), [solc](/man/solc)(1), [npm](/man/npm)(1)
