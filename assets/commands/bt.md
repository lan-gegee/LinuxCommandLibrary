# TAGLINE

Bittensor 区块链 CLI 工具

# TLDR

**查看钱包余额**

```btcli wallet balance --wallet.name [default]```

**列出**可用子网

```btcli subnets list```

**注册**到某个子网

```btcli subnets register --netuid [1] --wallet.name [default]```

**查看**质押信息

```btcli stake show --wallet.name [default]```

**转账** TAO 代币

```btcli wallet transfer --dest [address] --amount [1.0]```

# SYNOPSIS

**btcli** _command_ [_subcommand_] [_options_]

# DESCRIPTION

**btcli** 是 **Bittensor** 去中心化机器学习网络的命令行界面。它提供管理钱包、质押 TAO 代币、注册子网以及与 Bittensor 区块链交互的工具。

Bittensor 是一个为机器智能创建去中心化市场的协议，其中矿工提供计算资源，验证者评估质量。该 CLI 是参与者管理其网络参与的主要工具。

# CAVEATS

大多数操作前需要先创建 Bittensor 钱包。区块链操作涉及真实的加密货币和交易费用。网络注册可能需要工作量证明或回收 TAO。确认前务必核实交易详情。

# INSTALL

```apt: sudo apt install bootterm```

```brew: brew install bootterm```

```nix: nix profile install nixpkgs#bootterm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1)
