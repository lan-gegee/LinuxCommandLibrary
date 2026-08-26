# TAGLINE

来自 Foundry 的以太坊区块链交互工具

# TLDR

**查询地址的余额**

```cast balance [0x...address] --rpc-url [https://eth-mainnet.g.alchemy.com/v2/key]```

**调用合约函数**（只读）

```cast call [0x...contract] "balanceOf(address)" [0x...holder] --rpc-url [rpc_url]```

**发送交易**

```cast send [0x...contract] "transfer(address,uint256)" [0x...to] [amount] --rpc-url [rpc_url] --private-key [0x...]```

**解码交易输入数据**

```cast 4byte-decode [0x23b872dd...]```

**将 wei 转换为 ether**

```cast from-wei [1000000000000000000]```

**将 ether 转换为 wei**

```cast to-wei [1.5]```

**查询当前 gas 价格**

```cast gas-price --rpc-url [rpc_url]```

**解码 ABI 编码的数据**

```cast abi-decode "transfer(address,uint256)" [0x...]```

**查询函数签名**

```cast sig "transfer(address,uint256)"```

# SYNOPSIS

**cast** _subcommand_ [_options_]

# DESCRIPTION

**cast** 是一个用于与以太坊及 EVM 兼容区块链交互的命令行工具。它是 Foundry 工具集的一部分，提供查询链上状态、发送交易、编码/解码数据以及执行单位换算等实用功能。

Cast 可以通过调用 view 函数或发送改变状态的交易来与已部署的合约交互。它负责 ABI 编码/解码，让你可以方便地在命令行中操作智能合约。

该工具还提供处理以太坊数据格式的实用程序，包括 wei/ether 之间、十六进制/十进制之间的换算，以及各种编码方案。它还集成了类 Etherscan 服务用于签名查询。

# PARAMETERS

**call** _contract_ _sig_ [_args_]
> 调用合约函数（只读）。

**send** _contract_ _sig_ [_args_]
> 向合约发送交易。

**balance** _address_
> 查询地址的 ETH 余额。

**block** [_number_]
> 获取区块信息。

**tx** _hash_
> 获取交易详情。

**receipt** _hash_
> 获取交易回执。

**gas-price**
> 获取当前 gas 价格。

**abi-encode** _sig_ [_args_]
> 对函数调用数据进行 ABI 编码。

**abi-decode** _sig_ _data_
> 解码 ABI 编码的数据。

**sig** _signature_
> 获取函数选择器（4 字节）。

**4byte-decode** _selector_
> 查询函数签名。

**to-wei** _amount_
> 将 ether 转换为 wei。

**from-wei** _amount_
> 将 wei 转换为 ether。

**--rpc-url** _url_
> 以太坊 RPC 端点。

**--private-key** _key_
> 用于签名的私钥。

**--chain** _chain_
> 链名称或 ID。

# CONFIGURATION

**foundry.toml**
> 项目级 Foundry 配置，包括默认 RPC URL、链设置和 Etherscan API 密钥。

# CAVEATS

需要访问以太坊 RPC 端点。私钥应妥善保管（使用环境变量或 keystore）。复杂交易的 gas 估算可能不准确。部分函数在签名查询时需要 Etherscan API 密钥。

# HISTORY

**cast** 是 **Foundry** 的组成部分，由 **Georgios Konstantopoulos** 和 **Paradigm** 团队开发，于 **2021 年 12 月**发布。Foundry 是一个用 Rust 编写的快速、可移植的以太坊开发工具包，灵感来自 DappTools。Cast 提供命令行实用工具，Forge 负责测试，Anvil 提供本地节点。

# SEE ALSO

[forge](/man/forge)(1), [chisel](/man/chisel)(1), [geth](/man/geth)(1)
